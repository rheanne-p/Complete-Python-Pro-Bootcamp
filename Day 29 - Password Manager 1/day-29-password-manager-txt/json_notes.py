import json

with open("data.json", mode="r") as data_file:
    # 1. Reading Old Data
    data = json.load(data_file)

    # 2. Updating old data with new dict
    data.update(new_dict)  # converts json read to python dict
    # interchange serialize from json to python, vice versa

    # 3. Saving updated data
    with open("data.json", mode="w") as data_file:
        json.dump(data, data_file, indent=4)
