import csv

from random import random
from random import randint

hashtags = []

def get_hashtags ():
    with open('hashtags.csv') as hashtags_file:
        reader = csv.reader(hashtags_file, delimiter=',')
        row_count = 0
        for row in reader:
            if row_count != 0:
                hashtags.append(row[0])
            row_count =+ 1
        return hashtags

def write_hashtag (instagram_values):
    fieldnames = []
    with open('hashtags copy.csv', mode="r") as hashtags_file:
        reader = csv.DictReader(hashtags_file)
        row_count = 0
        for row in reader:
            if row_count == 0:
                fieldnames = list(row.keys())
            row_count += 1
    with open('hashtags copy.csv', mode="w") as hashtags_file:
        writer = csv.DictWriter(hashtags_file, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for value in instagram_values:
            writer.writerow({'instagram':value})



# with open('hashtags.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count != 0:
#             print(row)
#         line_count =+ 1
    
