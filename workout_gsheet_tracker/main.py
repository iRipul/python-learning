import requests
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
SHEETY_API = os.environ["SHEETY_API"]
SHEETY_API_URL = f"https://api.sheety.co/{SHEETY_API}/myworkout/workouts"
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]


def format_exercise_data(exercise):
    now = dt.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    return {
        "name": exercise["name"].title(),
        "duration_min": exercise["duration_min"],
        "nf_calories": exercise["nf_calories"],
        "date": date,
        "time": time
    }


def process_query(query):
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    params = {
        "query": query
    }
    headers = {
        "x-app-id": APP_ID,
        'x-app-key': APP_KEY
    }
    response = requests.post(exercise_endpoint, params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return [format_exercise_data(exercise) for exercise in data["exercises"]]


def get_workout_data():
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    response = requests.get(SHEETY_API_URL, headers=headers)
    response.raise_for_status()
    return response.json()


def insert_workout_data(data_obj):
    body = {
        "workout": {
            "date": f"{data_obj['date']}",
            "time": f"{data_obj['time']}",
            "exercise": f"{data_obj['name']}",
            "duration": f"{data_obj['duration_min']}",
            "calories": f"{data_obj['nf_calories']}",
        }
    }
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    response = requests.post(url=SHEETY_API_URL, json=body, headers=headers)
    response.raise_for_status()
    return response.status_code


query = input("Please tell me which exercise did you do today?\n")
result = process_query(query)
for task in result:
    print(insert_workout_data(task))

print("logged into the sheet successfully")

print(get_workout_data())
