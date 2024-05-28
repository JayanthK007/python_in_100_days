#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from datetime import datetime


data_manager=DataManager()

sheet_data=requests.get(url='https://api.sheety.co/98cfb9c67a9da2a976701279c77b3e52/flightDeals/prices')

data=[]
for flight_detail in sheet_data.json()['prices']:
    flight_search=FlightSearch(flight_detail)
    if flight_search.iataCode=="":
        data.append(flight_search.update_iataCode())
    else:
        data.append(flight_detail)


for detail in data:
    data_manager.update_sheet(detail)

flight_data=FlightData()

today=datetime.now()
this_year=int(today.strftime('%Y'))
this_month=int(today.strftime('%m'))
today_day=int(today.strftime('%d'))
if today_day<30:
    today_day+=1
else:
    today_day=1
    if this_month==12:
        this_month=1
    else:
        this_month+=1
        
for detail in data:
    flight_data.search_flights('LON',detail['iataCode'],datetime(year=this_year,month=this_month,day=(today_day)).strftime('%Y-%m-%d'))    


