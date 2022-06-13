#!/usr/bin/env python3
import csv
with open ('employee_birthday.csv','w') as csvfile:
        fieldnames = ['emp_name', 'dept', 'birth_month']
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},{'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})