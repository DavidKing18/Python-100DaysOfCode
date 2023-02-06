# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests

sheety_endpoint = "https://api.sheety.co/0ddc17c284692df155ab4b36a99c5004/flightDeals/prices"
ORIGIN_CITY_IATA = "LOS"

FLIGHT_CLUB_ENDPOINT = "https://api.sheety.co/0ddc17c284692df155ab4b36a99c5004/flightDeals/users"


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
        to_time=six_month_from_today,
        destination_city=destination["city"]
    )
    try:
        price = flight.price
    except AttributeError:
        pass
    else:
        if flight.price < destination["lowestPrice"]:
            message = f"\nLow price alert! Only £{flight.price} to fly from " \
                      f"{flight.origin_city}-{flight.origin_airport} to " \
                      f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " \
                      f"{flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\nFLight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
            response = requests.get(url=FLIGHT_CLUB_ENDPOINT).json()
            users = response["users"]
            for user in users:
                notification_manager.send_email(message=message, email=user["email"], from_code=ORIGIN_CITY_IATA,
                                                to_code=destination["iataCode"], out_date=flight.out_date,
                                                return_date=flight.return_date)
