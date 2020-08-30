import csv
import pprint

from csv_ops import get_data
from csv_ops import write_data
from statistics import mean

months = [
    "july 2020",
    "june 2020",
    "may 2020",
    "april 2020",
    "march 2020",
    "february 2020",
    "january 2020",
    "december 2019",
    "november 2019",
    "october 2019",
    "september 2019",
    "august 2019",
    "july 2019"
]
csv_files = ["./fb_analytics/july.csv"]
hours = ["month"] + list(range(24))

def get_avg (month, columns):
    data = get_data(file = "./fb_analytics/{}.csv".format(month), columns = columns)
    row = {}
    row["month"] = month
    for index, col in enumerate(columns):
        numbers = []
        for x in data:
            num = x[col]
            print(month, col, num)
            num = int(num)
            numbers.append(num)
        avg = mean(numbers)
        row[hours[index + 1]] = avg
    return row

def col_names ():
    col_names = []
    for x in range(24):
        name = "Daily Liked and Online - {}".format(x)
        col_names.append(name)
    return col_names

data_list = []
for index, data in enumerate(months):
    data = get_avg(
        month = months[index],
        columns = col_names()
    )
    data_list.append(data)
write_data("./csv/fb_online_times.csv", hours, data_list)



