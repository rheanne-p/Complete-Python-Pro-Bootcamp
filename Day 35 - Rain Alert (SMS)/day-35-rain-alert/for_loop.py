import requests

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 34.055856,
    "lon": -118.111663,
    "appid": "cde202df3ac0ed44f0ddb4b1c5435a43",
}

response = requests.get(url=OWN_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
data_list = data["list"]

entry_num = 0
twelve_hours_list = []

for _ in range(0, 4):
    current_entry = data_list[entry_num]["weather"][0]["id"]
    if current_entry < 700:
        print("Bring an umbrella! ☂️")
    entry_num += 1


