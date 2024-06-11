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


total_salary = sum(people['salary'] for people in peoples_data)
salaries_avg = total_salary/len(peoples_data)

peoples_output = []
for people in peoples_data:
    if people['salary'] >= salaries_avg:
        peoples_output.append(people)


output_file = 'AboveAVGPeoples.csv'
with open(output_file, mode = 'w', newline = '') as file:
    csv_writer = csv.writer(file, delimiter = ',')
    header = ['name', 'age', 'salary']
    csv_writer.writerow(header)
    for people in peoples_output:
        row = [people['name'], people['age'], people['salary']]
        csv_writer.writerow(row)


#test only
print(total_salary)
print(len(peoples_data))
print(salaries_avg)
print(peoples_output)