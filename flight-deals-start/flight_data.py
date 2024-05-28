from amadeus import Client, ResponseError
import dotenv
import os
from datetime import datetime, timedelta

dotenv.load_dotenv()

class FlightData:
    def __init__(self):
        self.amadeus = Client(
            client_id=os.getenv('AMADUS_API_KEY'),
            client_secret=os.getenv('AMADUS_SECRET')
        )
        self.flights = []

    def search_flights(self, origin, destination, start_date, months=1):
        

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        for month in range(months):
            search_date = start_date + timedelta(days=30*month)
            formatted_date = search_date.strftime("%Y-%m-%d")
            try:
                response = self.amadeus.shopping.flight_offers_search.get(
                    originLocationCode=origin,
                    destinationLocationCode=destination,
                    departureDate=formatted_date,
                    adults=1,
                    max=1,  # Adjust as needed
                    currencyCode="GBP"
                )
                # Append the flight offers to the list
                if len(response.data)>0:
                    self.flights.append({
                        "price": response.data[0]['price']['total'],
                        "origin_city": origin,
                        "destination_city": destination,
                        "out_date": search_date.strftime("%Y-%m-%d")
                    })
                else:
                    self.flights.append(f"There is no flight from {origin} to {destination} on {search_date.strftime("%Y-%m-%d")}")    
            except ResponseError as error:
                print(f"Error searching for flights on {formatted_date}: {error}")
        return self.flights

