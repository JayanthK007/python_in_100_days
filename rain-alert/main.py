
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()

api_key=os.getenv('api_key')
owm_url=os.getenv('owm_url')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
to_phone_number = os.getenv('my_num')


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
    to=to_phone_number,
    body="It's going to rain today. Please remember to bring ☔"
    )

    print(message.status)    