from twilio.rest import Client
import os

TWILIO_SID = "ACca0ea5bd6df26df15bd88fb8c9a86e0f"
TWILIO_AUTH_TOKEN = os.environ["AUTH_TOKEN"]

TWILIO_VIRTUAL_NUMBER = "+12058329459"
TWILIO_VERIFIED_NUMBER = '+2348083603251'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+12058329459",
            to='+2348083603251'
        )
        # Prints if successfully sent.
        print(message.sid, "SENT")
