import csv

countries_filename = 'country_info.txt'

with open(countries_filename, encoding='utf-8', newline='') as country_file:
    reader = csv.DictReader(country_file)
    for row in reader:
        print(row)