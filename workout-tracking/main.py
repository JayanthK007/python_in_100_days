import os
import requests
import dotenv
import datetime

dotenv.load_dotenv()

time=datetime.datetime.now()
day=(time.strftime('%d/%m/%Y'))
present_time=(time.strftime("%H:%M:%S"))

response=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",headers={
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
},json={
    'query':input('Tell me which exercise you did:')
})
print(response.json())


sheety_resp=requests.post(url='https://api.sheety.co/98cfb9c67a9da2a976701279c77b3e52/workoutTracking/workouts',headers={
    "Authorization": "Bearer "+os.getenv("SHEETY_AUTH")
},json={
    "workout":{
        "date":day,
        "time":present_time,
        "exercise":response.json()['exercises'][0]['name'].title(),
        "duration":response.json()['exercises'][0]['duration_min'],
        "calories":response.json()['exercises'][0]['nf_calories']
        }
})
print(sheety_resp.json())