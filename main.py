import os
import requests
import config

endpoint = "http://api.openweathermap.org/data/2.5/weather"
one_call = "https://api.openweathermap.org/data/2.5/onecall"  # ?lat={lat}&lon={lon}&exclude={part}&appid={API key}
parameters = {
    "lat": 35.9621,
    "lon": -79.7623,
    "appid": os.getenv("api_key"),
    "exclude": "current,minutely,daily"
}
response = requests.get(url=one_call, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    # print(hourly_data[0])
    if condition_code < 800:
        will_rain = True
    else:
        print(condition_code)

if will_rain:
    # for k, v in os.environ.items():
    #     print(f'{k}={v}')
    config.send_sms()


