import datetime as dt
import random
import smtplib
import pandas

PLACEHOLDER = "[NAME]"


def send_email(to_email, body, subject):
    email = "xxxxx@gmail.com"
    pwd = "xxxx"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=pwd)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )


now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
print(f"Today is {day}/{month}/{year}")
print("Lets check that we have someone's birthday today and wish them.")
bday_data = pandas.read_csv("birthdays.csv")
bday_buddies = bday_data[(bday_data.day == day) & (bday_data.month == month)]
if bday_buddies.empty:
    print("No Birthdays today.")
else:
    # pick a random letter
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as bday_mail:
        for index, row in bday_buddies.iterrows():
            name = row['name'].strip()
            email = row['email'].strip()
            contents = bday_mail.read()
            letter = contents.replace(PLACEHOLDER, name)
            send_email(to_email=email, subject="Happy Birthday!", body=letter)
