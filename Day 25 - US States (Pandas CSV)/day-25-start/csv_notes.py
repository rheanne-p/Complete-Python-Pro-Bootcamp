# in-built csv library
import csv

with open("weather_data.csv") as data_file:
    # csv.reader method takes file as argument
    # reads and outputs data
    # creates a csv reader object
    data = csv.reader(data_file)
    print(data)
    # can loop through csv reader object
    for row in data:
        # takes each row in weather.csv
        # separates each item as a single value
        print(row)
