import requests

class DataManager:
    def update_sheet(self,data):
        self.id=data['id']
        response=requests.put(url=f'https://api.sheety.co/98cfb9c67a9da2a976701279c77b3e52/flightDeals/prices/{self.id}',json={
            "price":data
        })
        print(response.text)