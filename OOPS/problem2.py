'''
Employee salary manager
create a class named as Employee
Requirements:
1.Private var - __salary
2.salary should not be < 1500
3.Method increase_salary(percent)

if invalid:
invalid salary

input:20000
percent:10
output: 22000



'''
class Employee:
    def __init__(self, salary):
        if salary < 1500:
            print("invalid salary")
            self.__salary = 0
        else:
            self.__salary = salary

    def increase_salary(self, percent):
        if self.__salary > 0:
            self.__salary = self.__salary + (self.__salary * percent / 100)
            print(int(self.__salary))

salary = int(input("Enter salary: "))
percent = int(input("Enter percent: "))

emp = Employee(salary)
emp.increase_salary(percent)