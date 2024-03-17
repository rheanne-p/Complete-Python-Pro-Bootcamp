import pandas

data = pandas.read_csv("weather_data.csv")
print("Print row:")
print(data[data.day == "Monday"])
