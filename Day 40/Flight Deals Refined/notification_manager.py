from twilio.rest import Client
import os
from smtplib import SMTP

TWILIO_SID = "ACca0ea5bd6df26df15bd88fb8c9a86e0f"
TWILIO_AUTH_TOKEN = os.environ["AUTH_TOKEN"]

TWILIO_VIRTUAL_NUMBER = "+12058329459"
TWILIO_VERIFIED_NUMBER = '+2348083603251'

my_email = "cornflakeschicago@gmail.com"
password = os.environ["CHICAGO_MAIL_PASSWORD"]

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

    def send_email(self, message, email, from_code, to_code, out_date, return_date):
        flight_link = f"https://www.google.co.uk/flights?hl=en#flt={from_code}.{to_code}.{out_date}" \
                      f"*{to_code}.{from_code}.{return_date}"
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: New Low Price Flight! "
                                                                        f"\n\n{message}\n{flight_link}".encode("utf-8"))
