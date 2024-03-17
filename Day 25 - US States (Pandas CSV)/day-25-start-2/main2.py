import pandas

data = pandas.read_csv("squirrel_data2.csv")

print("Executing main2.py")

gray_count = len(data[data.PrimaryFurColor == "Gray"])
red_count = len(data[data.PrimaryFurColor == "Cinnamon"])
black_count = len(data[data.PrimaryFurColor == "Black"])

count_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}
count_dataframe = pandas.DataFrame(count_dict)
count_dataframe.to_csv("squirrel_count2.csv")


# TODO: Difference
# Changed the Series title from "Primary Fur Color" to
# "PrimaryFurColor", so it can be called as an
# attribute instead of a String

# data["Primary Fur Color"] vs. data[data.PrimaryFurColor]
# the latter uses fewer lines
