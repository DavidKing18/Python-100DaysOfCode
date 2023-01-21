##################################
# Reading csv data in python.
##################################

# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))


##################################
# DataFrames and Series;
##################################
import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())  # average/mean of a series
#
# print(data["temp"].max())  # maximum value in series
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# temp_in_fahrenheit = 1.8 * monday_temp + 32
# print(temp_in_fahrenheit)

# Create a dataFrame from scratch

# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

