# csv represents tabular data (excel sheets)
# comma separated values (without spaces)

with open("weather_data.csv") as data_file:
    # takes each line, turns into item in a list
    data = data_file.readlines()
    # prints out data as a list
    # each item is a row in the list
    print(data)
