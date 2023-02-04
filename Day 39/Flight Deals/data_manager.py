import requests

sheety_endpoint = "https://api.sheety.co/0ddc17c284692df155ab4b36a99c5004/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_data(self):
        response = requests.get(sheety_endpoint).json()
        result = response['prices']
        return result

    def update_sheet(self, id, parameter):
        requests.put(f"{sheety_endpoint}/{id}", json=parameter)
