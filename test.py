import csv

print("Hello World")


with open('config.csv', 'r') as fd:
    reader = csv.reader(fd)
    
    for line in reader:
        print(line)