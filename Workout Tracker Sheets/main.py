import requests
import os
from datetime import datetime

APP_ID = "c1084b23"
APP_KEY = "d3e076e2b968a83b190c835bec9a66b3"
SHEETY_AUTH = "Bearer workoutwithme"
SHEETY_ENDPOINT = "https://api.sheety.co/2dc1f05fa072d962fdf0e72f212286c3/workoutTracking/workouts"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

today = datetime.now()

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

# os.environ["APP_ID"] = APP_ID
# os.environ["APP_KEY"] = APP_KEY
# os.environ["SHEETY_ENDPOINT"] = SHEETY_ENDPOINT
# os.environ["SHEETY_AUTH"] = SHEETY_AUTH

sheety_headers = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json"
}

nutritionix_params = {
    "query": input("What exercise did you do today?"),
    "gender": "male",
    "weight_kg": 82.5,
    "height_cm": 170,
    "age": 26,
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
print(nutritionix_response.text)


for exercise in nutritionix_response.json()["exercises"]:
    sheety_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
    print(sheety_response.text)