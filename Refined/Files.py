import csv

with open('ye.csv', 'r') as file:
    file_read = csv.reader(file) 

    for line in file_read:
        print(line)