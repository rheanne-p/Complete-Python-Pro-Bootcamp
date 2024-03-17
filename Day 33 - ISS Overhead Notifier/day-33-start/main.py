import requests

# get data from endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
# prints <Response [200]>
#                status code

if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data.")

# Response Codes:
# 404: trying to retrieve something that doesn't exist
# 100: hold on, something wrong is happening
# 200: here you go
# 300: no permission
# 400: you messed up (client error)
# 500: server messed up, server is down (server error)
