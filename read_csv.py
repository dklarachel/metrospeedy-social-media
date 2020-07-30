import csv

hashtags = []

def get_hashtags ():
    with open('hashtags.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        row_count = 0
        for row in readCSV:
            if row_count != 0:
                hashtags.append(row[0])
            row_count =+ 1

