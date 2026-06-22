'''
company wants to generate employee salary reports
1.Accept employee details
2.store them in employee.txt
3.calculate total salary expenditure
total = 0 + salary
4.display employee report

Sample Input:
enter the emp name : Anas
enter the salary: 50000

output:
Employee Report
Anas 50000
Total Expenditure:50000

'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

name = input("Enter the employee name: ")
salary = int(input("Enter the salary: "))

with open("employee.txt", "w") as file:
    file.write(f"{name},{salary}\n")

total = 0

with open("employee.txt", "r") as file:
    print("\nEmployee Report")

    for line in file:
        emp_name, emp_salary = line.strip().split(",")
        emp_salary = int(emp_salary)

        print(emp_name, emp_salary)

        total += emp_salary

print("Total Expenditure:", total)