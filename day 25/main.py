# with open("weather_data.csv") as file:
#     data=file.readlines()

# import csv

# with open('weather_data.csv') as file:
#     data=csv.reader(file)
#     temperature=[]
#     for row in data:
#         if row[1]!='temp':
#             temperature.append(int(row[1]))

# print(temperature)        

import pandas
# import statistics

# data=pandas.read_csv("weather_data.csv")
# temp_list=data["temp"].to_list()

# sunday=data[data.temp.max()==data.temp]
# print(sunday.temp[6])

data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
save_data=data['Primary Fur Color'].value_counts() 

csv_data=pandas.DataFrame(save_data)
print(csv_data.to_csv("squirrel.csv"))