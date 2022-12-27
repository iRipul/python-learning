import requests
import datetime as dt
from dateutil import tz
import math
import smtplib

MY_LOCATION = (<lat>, <long>)


def get_iss_location():
    ISS_API_END_POINT = "http://api.open-notify.org/iss-now.json"
    response = requests.get(ISS_API_END_POINT)
    response.raise_for_status()
    data = response.json()
    return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])


def check_if_night():
    LAT = MY_LOCATION[0]
    LONG = MY_LOCATION[1]
    SUNSET_SUNRISE_API_ENDPOINT = "https://api.sunrise-sunset.org/json"
    FORMATTED = 0

    parameters = {
        "lat": LAT,
        "lng": LONG,
        "formatted": FORMATTED
    }
    response = requests.get(SUNSET_SUNRISE_API_ENDPOINT, parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    now = dt.datetime.now(tz=tz.tzlocal())
    sunrise_ist = dt.datetime.fromisoformat(sunrise).astimezone(tz=tz.tzlocal())
    sunset_ist = dt.datetime.fromisoformat(sunset).astimezone(tz=tz.tzlocal())

    now_hour = now.hour
    sunrise_hour = sunrise_ist.strftime('%H')
    sunset_hour = sunset_ist.strftime('%H')
    if now_hour < int(sunrise_hour) or now_hour > int(sunset_hour):
        return True
    else:
        return False


def is_iss_near(iss_location, from_location):
    if from_location[0] - 5 <= iss_location[0] <= from_location[0] + 5 and \
            from_location[1] - 5 <= iss_location[1] <= from_location[1] + 5:
        return True
    else:
        return False


def send_email(to_email, body, subject):
    email = "xxx@gmail.com"
    pwd = "xxxxxx"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=pwd)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )


if is_iss_near(get_iss_location(), MY_LOCATION) and check_if_night():
    # send email
    print("Sending email....")
    send_email("xxxx@gmail.com", "ISS is near to you. "
                                           "Please look up and see the moving star!!", "ISS is nearby")
else:
    print("ISS is far from you")
