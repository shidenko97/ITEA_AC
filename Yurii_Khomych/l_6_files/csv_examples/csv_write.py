import csv

with open("employee_file.csv", mode="w") as employee_file:
    employee_writer = csv.writer(employee_file)

    employee_writer.writerow(["name", "job", "month"])
    employee_writer.writerow(["John Smith", "Accounting", "November"])
    employee_writer.writerow(["Erica Meyers", "IT", "March"])
