import requests
from datetime import datetime

USERNAME = "appbreweryday37"
TOKEN = "pixela_token"
GRAPH_ID = "graph"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Hours of Code",
    "unit": "mins",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# last_year = datetime(year=2021, month=10, day=24)
today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_config = {
    "date": today_formatted,
    "quantity": "40",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{today_formatted}"

update_config = {
    "quantity": "60",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)
delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
