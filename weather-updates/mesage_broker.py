import os
from twilio.rest import Client


class TwilioBroker:
    def __init__(self):
        self.from_number = "xxxxxxx"
        self.account_sid = "xxxxxx"
        self.auth_token = "xxxxxxxx"
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, message, to_number):
        message = self.client.messages.create(
                              body=message,
                              from_=self.from_number,
                              to=to_number
                          )
        return message
