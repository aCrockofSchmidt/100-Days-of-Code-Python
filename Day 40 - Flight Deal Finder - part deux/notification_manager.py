import smtplib
from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("TWILIO_ACCT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "+18482175388"
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_CELL_NUMBER")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.mail.yahoo.com"
MY_EMAIL = "the_legendary_flush@yahoo.com"
MY_PASSWORD = os.environ.get("YAHOO_PASSWORD")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="the.legendary.flush@gmail.com",
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8'), port=587
                )