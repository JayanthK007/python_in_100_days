
import requests
from twilio.rest import Client

api_key='api_key_needs_to added'
owm_url="https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'Twilio accound sid'
auth_token = 'auth token for twilio account'

parameters={
'lat':51.507351,
'lon':-0.127758,
'appid':api_key,
'cnt':4
}
response=requests.get(url=owm_url,params=parameters)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]['weather'][0]['id'])
will_rain=False
for hour_data in weather_data['list']:
    if int(hour_data['weather'][0]['id']) <700:
        will_rain=True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+17819902304',
    to='add_your number',
    body="It's going to rain today. Please remember to bring ☔"
    )

    print(message.status)    