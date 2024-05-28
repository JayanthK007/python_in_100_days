from amadeus import Client, ResponseError,Location
import dotenv
import os

dotenv.load_dotenv()



class FlightSearch:
    def __init__(self,flight_details) :
        self.city=flight_details['city']
        self.iataCode=flight_details['iataCode']
        self.id=flight_details['id']
        self.lowestPrice=flight_details['lowestPrice']


    def update_iataCode(self)-> dict:
        amadeus = Client(
        client_id=os.getenv('AMADUS_API_KEY'),
        client_secret=os.getenv('AMADUS_SECRET')
        )

        try:
            '''
            Which cities or airports start with 'r'?
            '''
            response = amadeus.reference_data.locations.get(page={'limit':1},
                                                            keyword=self.city,
                                                            subType=Location.CITY,
                                                            view="LIGHT"
                                                            )
            
        except ResponseError as error:
            raise error
        self.iataCode=response.data[0]['iataCode']
        return {'city':self.city,'iataCode':self.iataCode,'id':self.id,'lowestPrice':self.lowestPrice}