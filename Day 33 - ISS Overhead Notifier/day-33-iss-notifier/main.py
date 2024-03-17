import requests
from datetime import datetime
import smtplib

MY_LAT = 34.0522
MY_LONG = -118.2437

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour
print(hour)


near = False
dark = False


def close():
    global close
    if iss_longitude == MY_LONG + 5 or iss_longitude == MY_LONG - 5 and iss_latitude == MY_LAT + 5 or MY_LAT - 5:
        close = True


def dark():
    global dark
    if hour < sunrise and hour > sunset:
        dark = True


near()
dark()

if near and dark:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="appbreweryday32@gmail.com", password="zfzxmqlknzqjkfbf")
        connection.sendmail(
            from_addr="appbreweryday32@gmail.com",
            to_addrs="pythonrecipientday32@yahoo.com",
            msg="Subject:ISS Notification\n\nLook up, the ISS is right above!"
        )
