import requests

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": 34.055856,
    "lon": -118.111663,
    "appid": "cde202df3ac0ed44f0ddb4b1c5435a43",
}

response = requests.get(url=OWN_ENDPOINT, params=parameters)
response.raise_for_status()
current_weather = response.json()
print(current_weather)
