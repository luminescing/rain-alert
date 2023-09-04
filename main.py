import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "{api_key}"
account_sid = "{account_sid}"
auth_token = "{auth_token}"


weather_params = {
    "lat": {your_lat},
    "lon": {your_lon},
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today! Remember to bring an umbrella. ☂️",
                        from_="{automated_number}",
                        to="{your_number}"
                    )