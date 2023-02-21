# write a program that reads in a CSV file and prints out the contents of the file

with open('country_medals.csv', encoding='utf-8', newline='') as file:
    for line in file:
        print(line.strip())