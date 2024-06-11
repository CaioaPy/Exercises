#Objective: Read from and write to CSV files using Python.

#Instructions:

#Read data from a CSV file containing columns name, age, and salary.
#Compute the average salary of all individuals in the file.
#Write a new CSV file that includes only individuals with a salary above the average.

import csv

input_file = 'peoples.csv'
people = []
salaries = []

with open(input_file, mode = 'r', newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        row['salary'] = int(row['salary'])
        salaries.append(row['salary'])

total_salary = 0
for salary in salaries:
    total_salary += salary
salaries_avg = total_salary/len(salaries)

above_avg_salaries = []
for salary in salaries:
    if salary >= salaries_avg:
        above_avg_salaries.append(salary)

output_file = 'AboveAVGPeoples.csv'
with open(output_file, mode = 'w', newline = '') as file:
    csv_writer = csv.writer(output_file, delimiter = ',')
    for salary in above_avg_salaries:
        csv_writer.writerow()

#test only
print(total_salary)
print(len(salaries))
print(salaries_avg)
print(above_avg_salaries)