import requests
import smtplib

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 1.3521,  # 34.055856
    "lon": 103.8198,  # -118.111663
    "appid": "cde202df3ac0ed44f0ddb4b1c5435a43",
}

response = requests.get(url=OWN_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

will_rain = False

for entry in weather_slice:
    entry_id = entry["weather"][0]["id"]
    if entry_id < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="appbreweryday32@gmail.com", password="zfzxmqlknzqjkfbf")
        connection.sendmail(
            from_addr="appbreweryday32@gmail.com",
            to_addrs="appbreweryday32@gmail.com",
            msg="Subject:Rain\n\nBring an umbrella today!"
        )
