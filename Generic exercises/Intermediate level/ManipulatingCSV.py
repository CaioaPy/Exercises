#Objective: Read from and write to CSV files using Python.

#Instructions:

#Read data from a CSV file containing columns name, age, and salary.
#Compute the average salary of all individuals in the file.
#Write a new CSV file that includes only individuals with a salary above the average.

import csv

input_file = 'peoples.csv'
peoples_data = []

with open(input_file, mode = 'r', newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        row['salary'] = int(row['salary'])
        row['age'] = int(row['age'])
        peoples_data.append(row)

total_salary = 0
for salary in salaries:
    total_salary += salary
salaries_avg = total_salary/len(salaries)

above_avg_salaries = []
above_avg_salaries_people = []
for i in range(len(salaries)):
    if salaries[i] >= salaries_avg:
        above_avg_salaries.append(salaries[i])
        above_avg_salaries_people.append(peoples[i])

peoples_output = []
for people in peoples:
    if people['salary'] > salaries_avg:
        peoples_output.append(people)

"""
output_file = 'AboveAVGPeoples.csv'
with open(output_file, mode = 'w', newline = '') as file:
    csv_writer = csv.writer(file, delimiter = ',')
    header = ['name', 'salary']
    csv_writer.writerow(header)
    for i in range(len(above_avg_salaries)):
        row = [above_avg_salaries_people[i]['name'], above_avg_salaries[i]['salary']]
        csv_writer.writerow(row)

"""
#test only
print(total_salary)
print(len(salaries))
print(salaries_avg)
print(above_avg_salaries)
print(above_avg_salaries_people)
print(peoples_output)