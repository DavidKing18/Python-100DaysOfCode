#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from pprint import pprint
import requests

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheety_endpoint = "https://api.sheety.co/0ddc17c284692df155ab4b36a99c5004/flightDeals/prices"
ORIGIN_CITY_IATA = "NIG"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_data()

for city in sheet_data:
    if city["iataCode"] == "":
        flight_search = FlightSearch()
        iata_code = flight_search.get_iataCode(city_name=city["city"])
        data = {
            "price": {
                "iataCode": iata_code
            }
        }
        data_manager.update_sheet(id=city["id"], parameter=data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                    f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} "
                    f"to {flight.return_date}."
        )
