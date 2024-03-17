import json

# JavaScript Object Notation
# nested lists and dictionaries
# key: value pair structure

website = "website123.com"
email = "example@gmail.com"
password = "pass123"

new_data = {
    website: {
        "email": email,
        "password": password,
    }
}

with open("data.json", "r") as data_file:
    # Read:          file_path
    data = json.load(data_file)  # takes json data, converts to python dict
    # Update: new_data
    data.update(new_data)

with open("data.json", "w") as data_file:
    # Write: data dict  json file
    json.dump(data, data_file, indent=4)


# 1. reading old data
# 2. updating old data (with new data)
# 3. saving updated data to json file
