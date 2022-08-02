import os

import requests
from twilio.rest import Client
import os


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

account_sid = "AC7bfad92a7d8c6c80bbc36d26aab22574"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 51.048615,
    "lon": -114.070847,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key,
}

#response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=51.048615&lon=-114.070847&appid=626a0d3b4dc12dd9ad2b9f76a7588a7c")

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for days in range(47):
    if weather_data["hourly"][days]["weather"][0]["id"] < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+18482175388',
        to='+15877774433'
    )
    print(message.status)

