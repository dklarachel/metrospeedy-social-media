import csv
from csv_ops import get_data
from csv_ops import write_data

x_vars = ['time', 'impressions', 'engagements', 'engagement rate']

csv_files = [
    "./twitter_insights/1.csv",
    "./twitter_insights/2.csv",
    "./twitter_insights/3.csv"
]

data_list = []
for file in csv_files:
    data_list += get_data(file, x_vars)
write_data ("twitter_analytics.csv", x_vars, data_list)






