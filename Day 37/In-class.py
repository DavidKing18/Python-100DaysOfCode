import requests
from datetime import datetime

USERNAME = "oluwanifemi"
TOKEN = "C6U896d547TFF69658FIOYr"
GRAPH_ID = "graph1"

# Posting/Uploading data

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "mins",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many minutes did you code for today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


# Updating/Modifying data
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230202"

pixel_update_data = {
    "quantity": "90"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)


# Removing/Deleting data
pixel_remove_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230202"

# response = requests.delete(url=pixel_remove_endpoint, headers=headers)
# print(response.text)
