import requests
import datetime as dt
response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this data")
#
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
position = response.json()["iss_position"]
print(position)
#
# longitude = response.json()["iss_position"]["longitude"]
# print(longitude)
#
# latitude = response.json()["iss_position"]["latitude"]
# print(latitude)
#
# iss_position = (longitude, latitude)
# print(iss_position)

# parameters = {
#     "lat": 6.524379,
#     "lng": 3.379206,
#     "formatted": 0
# }
#
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
# sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
# print(sunrise)
# sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])
# print(sunset)
#
# current_time = dt.datetime.now().hour
# print(current_time)
