import os
import requests


class WeatherClient:
    def __init__(self):
        self.api_url = "https://api.openweathermap.org/data/2.5/onecall"
        self.api_key = "xxxxxxxxxxxxxx"

    def get_weather_data(self, location, params={}):
        lat = location[0]
        long = location[1]
        params["lat"] = lat
        params["lon"] = long
        params["appid"] = self.api_key
        response = requests.get(self.api_url, params)
        response.raise_for_status()
        data = response.json()
        return data
