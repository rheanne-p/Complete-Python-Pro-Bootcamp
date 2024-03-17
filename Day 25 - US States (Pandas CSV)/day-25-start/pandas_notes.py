import pandas

# reads csv file without opening it
data = pandas.read_csv("weather_data.csv")

# prints data as a table with indexes
print(data)

# prints all data in specified column
print(data["temp"])
# Syntax: DataFrame["series"]

# type checks
print(type(data))
# pandas DataFrame object


# 2 primary data structures: Series, DataFrame

# DataFrame:
# equivalent of entire table (every sheet or excel)

# Series:
# type check on "temp"
# pandas series object
# equivalent to a list, single column in table

# Data Structure Summary:
# entire table: DataFrame
# every column: Series (list)


# convert DataFrame to dictionary
print("DataFrame to Dictionary:")
data_dict = data.to_dict()
print(data_dict)
# each column as a separate dictionary

# convert Series to list
print("Series to List:")
temp_list = data["temp"].to_list()
print(temp_list)
