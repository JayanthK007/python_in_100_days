class FlightSearch:
    def __init__(self,flight_details) :
        self.city=flight_details['city']
        self.iataCode=flight_details['iataCode']
        self.id=flight_details['id']
        self.lowestPrice=flight_details['lowestPrice']


    def update_iataCode(self)-> dict:
        self.iataCode="Testing"
        return {'city':self.city,'iataCode':self.iataCode,'id':self.id,'lowestPrice':self.lowestPrice}