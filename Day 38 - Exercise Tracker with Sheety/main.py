import requests
import os
from datetime import datetime as dt

APP_ID = os.environ["NUT_APP_ID"]
API_KEY = os.environ["NUT_API_KEY"]
SHEETY_BEARER_TOKEN = os.environ["SHEET_TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me which exercises you did today: ")

parameters = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 84,
    "height_cm": 183,
    "age": 50
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# add new exercise data to spreadsheet using sheety API

date = dt.today()

sheety_add_endpoint = "https://api.sheety.co/9c077823f4a0bc977f741112cd401f88/workoutTracking/workouts"

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    exercise_inputs = {
        "workout": {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%H:%M:%S"),
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }
    exercise_response = requests.post(url=sheety_add_endpoint, json=exercise_inputs, headers=bearer_headers)

print(exercise_response.text)
