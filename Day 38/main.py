import os
import requests
from datetime import datetime as dt

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY"]
TOKEN = os.environ['Sheety_Token']

GENDER = "MALE"
WEIGHT_KG = "85"
HEIGHT = "190"
AGE = "20"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()

sheety_endpoint = "https://api.sheety.co/0ddc17c284692df155ab4b36a99c5004/workoutTracking/workouts"

now = dt.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

header = {"Authorization": TOKEN}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=header)
    sheety_response.raise_for_status()
    print(sheety_response.text)
