#Objective: Read from and write to CSV files using Python.

#Instructions:

#Read data from a CSV file containing columns name, age, and salary.
#Compute the average salary of all individuals in the file.
#Write a new CSV file that includes only individuals with a salary above the average.

import csv

file = 'peoples.csv'
people = []

with open(file, mode = 'r', newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        row['age'] = int(row['age'])
        row['salary'] = int(row['salary'])
        print(row['age'])
        print(row['salary'])