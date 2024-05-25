#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
import requests
from flight_search import FlightSearch
from data_manager import DataManager


data_manager=DataManager()

sheet_data=requests.get(url='https://api.sheety.co/98cfb9c67a9da2a976701279c77b3e52/flightDeals/prices')

data=[]
for flight_detail in sheet_data.json()['prices']:
    flight_search=FlightSearch(flight_detail)
    if flight_search.iataCode=="":
        data.append(flight_search.update_iataCode())

for detail in data:
    data_manager.update_sheet(detail)

