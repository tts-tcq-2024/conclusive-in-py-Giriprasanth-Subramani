from temperature_breach_classification import classify_temperature_breach
from send_alert import send_alert

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  alert_target = {
      'TO_CONTROLLER':send_alert.send_to_controller,
      'TO_EMAIL':send_alert.send_to_email
      }
  if alertTarget not in alert_target:
        raise ValueError(f'Invalid alert Type:{alertTarget}')
  alert_target[alertTarget](breachType)
