import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# called on response
# raise HTTPError if response was unsuccessful
response.raise_for_status()

# retrieves actual data, not response code
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
