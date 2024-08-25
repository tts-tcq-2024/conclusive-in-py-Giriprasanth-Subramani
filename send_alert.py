breach_type = {
    'TOO_LOW': 'Hi, the temperature is too low',
    'TOO_HIGH':'Hi, the temperature is too high'
    }

class send_alert:

    def print_on_console(message):
        print(message)

    def send_to_controller(breachType):
        header = 0xfeed
        message = f'{header}, {breachType}'
        send_alert.print_on_console(message)
   
    def send_to_email(breachType):
        recepient = "a.b@c.com"
        if breachType in breach_type:
            message = f'To: {recepient}\n'+breach_type[breachType]
        else:
            message = f'To: {recepient}\n'+breachType
        send_alert.print_on_console(message)

