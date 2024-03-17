import pandas

data = pandas.read_csv("squirrel_data.csv")

print("Executing the original main.py")

fur_colors_list = data["Primary Fur Color"].to_list()

gray_count = 0
red_count = 0
black_count = 0

for fur_color in fur_colors_list:
    if fur_color == "Gray":
        gray_count += 1
    elif fur_color == "Cinnamon":
        red_count += 1
    elif fur_color == "Black":
        black_count += 1

fur_count_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}

fur_count_dataframe = pandas.DataFrame(fur_count_dict)
fur_count_dataframe.to_csv("squirrel_count.csv")