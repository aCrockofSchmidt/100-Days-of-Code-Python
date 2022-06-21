# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# #print(data_dict)
#
# temp_list = data["temp"].to_list()
# #(temp_list)
#
# # find average temperature
#
# average_temperature = sum(temp_list) / len(temp_list)
# print(average_temperature)
#
# # this is how I initially did it and it's obviously way too convoluted
# total_temps = 0
# for temp in temp_list:
#     total_temps += temp
# average_temp = total_temps / len(temp_list)
# print(average_temp)
#
# # or just use pandas!
# print(data["temp"].mean())
#
# # get max challenge
#
# print(data["temp"].max())
#
# # get data in rows
#
# print(data[data.day == "Monday"])
#
# # print row with highest temperature
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # get monday's temperature converted to fahrenheit
#
# monday_temp_F = (monday.temp * 9 / 5) + 32
# print(monday_temp_F)
#
# # how to create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# create a CSV called squirrel count that reveals the total number of squirrels of each colour

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data.columns.values)

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

