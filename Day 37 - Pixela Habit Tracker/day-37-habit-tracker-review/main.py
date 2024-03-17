import requests
from datetime import datetime

USERNAME = "appbreweryday37review"
TOKEN = "pixela_token"
GRAPH_ID = "graph1"

# TODO 0. Header (Authentication)
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}


# TODO 1. Create User
pixela_endpoint = "https://pixe.la/v1/users"
create_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=create_params)
# print(response.text)


# TODO 2. Create New Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Minutes of Python",
    "unit": "mins",
    "type": "int",
    "color": "ajisai",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=HEADERS)
# print(response.text)


# TODO 3. Add Pixel
add_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

datetime_obj = datetime.now()
formatted_date = str(datetime_obj).replace("-", "").split()[0]

add_params = {
    "date": datetime_obj.strftime("%Y%m%d"),
    "quantity": "101",
}

# response = requests.post(url=add_endpoint, json=add_params, headers=HEADERS)
# print(response.text)


# TODO 4. Update Pixel
update_endpoint = f"{add_endpoint}/{formatted_date}"

update_params = {
    "quantity": "127"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=HEADERS)
# print(response.text)

# TODO 5. Delete Pixel
delete_endpoint = f"{add_endpoint}/20221210"

response = requests.delete(url=delete_endpoint, headers=HEADERS)
print(response.text)