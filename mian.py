# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)
#
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas


d = pandas.read_csv("data.csv")
# print(data["temp"])
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['condition'])
# print(data.condition)
# print(data[data.day == 'Monday'])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# monday_temp += (9/5) + 32
# print(monday_temp)

gray = len(d[d["Primary Fur Color"] == "Gray"])
red = len(d[d["Primary Fur Color"] == "Cinnamon"])
black = len(d[d["Primary Fur Color"] == "Black"])

print(gray)
print(red)
print(black)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("new_data.csv")
