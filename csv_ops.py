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

def write_hashtags (instagram_values, linkedin_values):
    fieldnames = []
    with open('hashtags.csv', mode="r") as hashtags_file:
        reader = csv.DictReader(hashtags_file)
        row_count = 0
        for row in reader:
            if row_count == 0:
                fieldnames = list(row.keys())
            row_count += 1
    with open('hashtags copy.csv', mode="w") as hashtags_file:
        writer = csv.DictWriter(hashtags_file, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        # for index, value in enumerate(instagram_values):
        #     writer.writerow({
        #         'hashtag': hashtags[index],
        #         'instagram': value
        #     })
        for value in instagram_values:
            writer.writerow({
                'hashtag': value,
                'instagram': instagram_values[value],
                'linkedin': linkedin_values[value]
            })
        print(instagram_values)
        print(linkedin_values)

def get_data (file, columns):
    '''gets data for specified columns (inputted as a list)'''
    with open(file, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        row_count = 0
        for row in reader:
            for col in columns:
                if col == "time":
                    value = row[col][11:16]
                else:
                    value = row[col]
                print("{} is {}".format(col, value))
            row_count += 1



# with open('hashtags.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count != 0:
#             print(row)
#         line_count =+ 1
    
