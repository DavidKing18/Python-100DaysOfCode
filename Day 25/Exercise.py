####################################################################
#  The Great Squirrel Census Data Analysis (with Pandas!)
####################################################################

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrel_fur_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}
squirrel_fur_data_csv = pandas.DataFrame(squirrel_fur_data)
squirrel_fur_data_csv.to_csv("squirrel_count.csv")
