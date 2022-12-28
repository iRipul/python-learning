from weather_client import WeatherClient
from mesage_broker import TwilioBroker

twilio = TwilioBroker()
wc = WeatherClient()

my_location = (40.49, 51.47)
weather_data = wc.get_weather_data(my_location, {"exclude": "minutely,daily"})["hourly"][:12]

hourly_rain_data = [data["weather"][0]["description"] for data in weather_data if data["weather"][0]["id"] <  700]

if len(hourly_rain_data) > 0:
    response = twilio.send_message("Hey! it is going to rain in next 12 hours. Please keep an ☂️ with you.",
                        "+xxxxxxxxxxx")
    print(response)
else:
    print("No Rain in next 12 hours")