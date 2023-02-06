##########################################################################################
#           Using API Keys to Authenticate and Get the Weather from OpenWeatherMap
##########################################################################################
import os
import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ["OWN_API_KEY"]  # Understanding Environment Variables and Hiding API Keys

account_sid = "ACca0ea5bd6df26df15bd88fb8c9a86e0f"
auth_token = os.environ["AUTH_TOKEN"]  # Environment Variable

MY_EMAIL = "cornflakeschicago@gmail.com"
PASSWORD = "tsjkmtsobmqbolxg"
RECEIVER_ADDRESS = "davidoadeleke90@gmail.com"

weather_params = {
    "lat": 6.451760,
    "lon": 3.089410,
    "appid": api_key,
    "exclude": "current,minutely,daily"
    }

response = requests.get(OWN_Endpoint, params=weather_params)
weather_condition = response.json()

will_rain = False
weather_slice = weather_condition["hourly"][:12]
for condition in weather_slice:
    condition_id = condition["weather"][0]["id"]
    if condition_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+12058329459",
        to='+2348083603251'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's not going to rain today. Raincheck!🥴",
        from_="+12058329459",
        to='+2348083603251'
    )
    print(message.status)
