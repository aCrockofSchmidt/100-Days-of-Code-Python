import requests
from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get("TWILIO_ACCT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_notification(
            self,
            cost,
            departure_city,
            departure_airport,
            destination_city,
            destination_airport,
            departure_date,
            return_date
    ):
        """ this method sends an SMS message when called"""

        message = self.client.messages.create(
            body=f"LOW PRICE ALERT! Only £{cost} to fly from {departure_city}-{departure_airport} to "
                 f"{destination_city}-{destination_airport}, from {departure_date} to {return_date}",
            from_="+18482175388",
            to="+15877774433"
        )
        print(message.status)
