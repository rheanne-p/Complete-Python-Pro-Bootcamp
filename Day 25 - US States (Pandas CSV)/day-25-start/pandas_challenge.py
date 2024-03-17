import pandas

data = pandas.read_csv("weather_data.csv")
# pandas.read_csv turns csv into a Panda object
# New Panda object contains DataFrame and several Series


# TODO 1: Find average of all temperatures
print("Average of Temperatures:")
temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# Mean Method
print("Mean Method:")
print(data["temp"].mean())

# TODO 2. Maximum temperature value
print("Maximum Temp's Value:")
print(data["temp"].max())

# Get Data in Columns
print("Square-Bracket Notation:")
print(data["condition"])
# square-bracket notation must exactly match String's case
# taps into the "condition" Series


# Panda converted columns into attributes
# of the DataFrame object
print("Attribute Retrieval:")
print(data.condition)
# treating data more like an object

# Get hold of data in row
print("Print row:")
print(data[data.day == "Monday"])
# DataFrame[column_attribute == "condition"]

# TODO 3. Print the row of data that has the highest temp
print("Highest Temperature's Row:")
print(data[data.temp == data.temp.max()])

# get hold of data frame, square brackets, get entire column, filter by a condition
# condition: when column is equal to a particular value: retrieves row


# TODO 4. Convert Monday's temp to Fahrenheit:
print("Monday's Temp to Fahrenheit:")
monday = data[data.day == "Monday"]
print(monday.condition)
monday_fahrenheit = int(monday.temp) * 9/5 + 32
print(monday_fahrenheit)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# Dictionary to Panda Object (DataFrame)
student_data = pandas.DataFrame(data_dict)

# Dictionary to CSV File
student_data.to_csv("new_data.csv")
