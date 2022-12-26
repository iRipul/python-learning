import smtplib
from random import randint
import datetime as dt


def send_email(to_email, body, subject):
    email = "xxxxxxxxxx@gmail.com"
    pwd = "xxxxxxxxxx"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=pwd)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )


def get_random_quote():
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        return quotes[randint(0, len(quotes) - 1)]


now = dt.datetime.now()
if now.weekday() == 0:
    quote = get_random_quote()
    send_email(to_email="xxxxxxxxxxxxx@gmail.com", subject="Monday Motivational Quote", body=get_random_quote())
