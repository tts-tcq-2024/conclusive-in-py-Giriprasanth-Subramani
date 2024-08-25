import unittest
import typewise_alert
import check_breach
import temperature_breach_classification
from unittest.mock import patch
import send_alert


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(check_breach.infer_breach(20, 50, 100) == 'TOO_LOW')
        self.assertTrue(check_breach.infer_breach(45, 20, 60) == 'NORMAL')
    def test_classify_temperature_breach_as_per_value(self):
        self.assertTrue(temperature_breach_classification.classify_temperature_breach('HI_ACTIVE_COOLING',-5) == 'TOO_LOW')
        self.assertTrue(temperature_breach_classification.classify_temperature_breach('MED_ACTIVE_COOLING',30) == 'NORMAL')
        self.assertTrue(temperature_breach_classification.classify_temperature_breach('PASSIVE_COOLING',55) == 'TOO_HIGH')
        with self.assertRaises(ValueError) as context:
            temperature_breach_classification.classify_temperature_breach('LOW_ACTIVE_COOLING',55)
        self.assertEqual(str(context.exception), "Invalid cooling type:LOW_ACTIVE_COOLING")
    @patch('builtins.print')
    def test_check_and_alert_as_per_values(self,mock_print):
        typewise_alert.check_and_alert('TO_EMAIL',{'coolingType': 'PASSIVE_COOLING'}, 75)
        mock_print.assert_called_with('To: a.b@c.com\nHi, the temperature is too high')
        typewise_alert.check_and_alert('TO_CONTROLLER',{'coolingType': 'HI_ACTIVE_COOLING'}, 40)
        mock_print.assert_called_with('65261, NORMAL')
        typewise_alert.check_and_alert('TO_EMAIL',{'coolingType': 'MED_ACTIVE_COOLING'}, -5)
        mock_print.assert_called_with('To: a.b@c.com\nHi, the temperature is too low')
        with self.assertRaises(ValueError) as context:
            typewise_alert.check_and_alert('TO_SMS',{'coolingType': 'HI_ACTIVE_COOLING'}, 40)
        self.assertEqual(str(context.exception), "Invalid alert Type:TO_SMS")    
    @patch('builtins.print')
    def test_send_alert_to_controller(self,mock_print):
        send_alert.send_alert.send_to_controller('TOO_LOW')
        mock_print.assert_called_with('65261, TOO_LOW')
        send_alert.send_alert.send_to_controller('HIGH')
        mock_print.assert_called_with('65261, HIGH')
    @patch('builtins.print')
    def test_send_alert_to_email(self,mock_print):
        send_alert.send_alert.send_to_email('TOO_LOW')
        mock_print.assert_called_with('To: a.b@c.com\nHi, the temperature is too low')
        send_alert.send_alert.send_to_email('NORMAL')
        mock_print.assert_called_with('To: a.b@c.com\nNORMAL') 
     
        
        


if __name__ == '__main__':
  unittest.main()
