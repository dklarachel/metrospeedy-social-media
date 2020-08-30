import csv
import pprint

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
    '''gets data for specified columns (inputted as a list), outputs list of dictionaries {'column':'item'}'''
    data_list = []
    with open(file, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data = {}
            for col in columns:
                if col == "time":
                    value = row[col][11:16]
                else:
                    value = row[col]
                data[col] = value
            data_list.append(data)
        return data_list

def write_data (file, fieldnames, data):
    ''' fieldnames parameter is a list, data parameter is a list of dictionaries , each list item is a row'''
    with open(file, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for dict in data:
            writer.writerow(dict)



# with open('hashtags.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count != 0:
#             print(row)
#         line_count =+ 1

def get_col (file, series, column):
    '''takes in series as col title, get data from specified column, returns dictionary {'series:'col_item'}'''
    data = {}
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                key = row[series]
                value = row[column]
                data[key] = value
            line_count += 1
        return data

def get_col_names (file, first_col=False):
    '''get names of columns, option to exclude first column, default is False for first_col'''
    with open (file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        row_count = 0
        for row in csv_reader:
            if row_count == 0:
                col_names = list(row.keys())
                if not first_col:
                    col_names.remove(col_names[0])
            row_count += 1
        return col_names
        
def write_data_from_list (file, fieldnames, list):
    '''
    write data from a list of lists to a column
    each list is a column
    '''
    with open(file, mode="w") as csv_file:
        writer = csv.writer(csv_file, lineterminator = '\n')
        for sub_list in list:
            writer.writerow(sub_list)



        

    
