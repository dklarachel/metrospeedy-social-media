import csv
# from csv_ops import get_data

x_vars = ['time', 'impressions', 'engagements', 'engagement rate']

csv_files = [
    "./twitter_insights/1.csv",
    "./twitter_insights/2.csv",
    "./twitter_insights/3.csv"
]

def get_data (file, columns):
    '''gets data for specified columns (inputted as a list)'''
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
    ''' data parameter is a list of dictionaries '''
    with open(file, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for dict in data:
            writer.writerow({
                fieldnames[0]: dict[fieldnames[0]],
                fieldnames[1]: dict[fieldnames[1]],
                fieldnames[2]: dict[fieldnames[2]],
                fieldnames[3]: dict[fieldnames[3]]
            })

data_list = []
for file in csv_files:
    data_list += get_data(file, x_vars)
write_data ("test twitter.csv", x_vars, data_list)

        




