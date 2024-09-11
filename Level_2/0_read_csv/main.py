from csv import reader

from numpy.ma.extras import average
from pandas import read_csv, DataFrame

temperature_data = []

with open("resources/weather_data.csv") as weather_file:
    line = 0
    while True:
        weather = weather_file.readline()
        if not weather:
            break
        if line != 0:
            temperature_data.append(int(weather.split(",")[1]))
        line += 1

print(temperature_data)

temperature_data = []

# treating as csv

with open("resources/weather_data.csv") as weather_file:
    values = reader(weather_file)
    for row in values:
        if row[1] != "temp":
            temperature_data.append(int(row[1]))

print(temperature_data)


# Pandas

data = read_csv("resources/weather_data.csv")
# print(data["temp"].values.tolist())

# print(type(data)) # <class 'pandas.core.frame.DataFrame'>
# print(type(data["temp"])) # <class 'pandas.core.series.Series'>

"""
[
{'day': 'Monday', 'temp': 12, 'condition': 'Sunny'}, 
{'day': 'Tuesday', 'temp': 14, 'condition': 'Rain'}, 
{'day': 'Wednesday', 'temp': 15, 'condition': 'Rain'}, 
{'day': 'Thursday', 'temp': 14, 'condition': 'Cloudy'}, 
{'day': 'Friday', 'temp': 21, 'condition': 'Sunny'}, 
{'day': 'Saturday', 'temp': 22, 'condition': 'Sunny'}, 
{'day': 'Sunday', 'temp': 24, 'condition': 'Sunny'}
]
"""
# print(data.to_dict(orient="records"))

# calculate average of the temperature
sum_of_temperatures = 0
count = 0
temperatures = data["temp"].to_list()
for temperature in temperatures:
    sum_of_temperatures += temperature
    count += 1

print(sum_of_temperatures / count)


# using inbuilt function
average_of_temperatures = sum(temperatures) / len(temperatures)
print(average_of_temperatures)

# using panda

print(data["temp"].mean())
print(data.temp.mean())

# get data conditionally

monday = data[data["day"] == "Monday"]
monday_temp = monday["temp"][0]
print(monday_temp)



# create a DataFrame

data_dict = {
    "students" : ["A","B","C"],
    "score" : [1,2,3]
}

data = DataFrame(data_dict)
data.to_csv("resources/student_scores.csv")



