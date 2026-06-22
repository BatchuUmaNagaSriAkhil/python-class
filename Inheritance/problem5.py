'''
Employee Bonus Mgmt
A company wants to calc
yearly bonuses for 
different types of employees 

create a base class Employee:
with:
name , salary 
create method:
calculate bonus()

then create two child classes 
developer
Bonus = 20% of salary 
manager 
Bonus = 35% of salary 
write a program to:
1.Take employee details as input
2.create objects based on employee type
3.Display:
employee name 
role
Bonus amount 

input format:
role,name,salary

output format:
Name:<name>
Role:<role>
Bonus:<bonus>

Sample:
3
Developer Rahu1 50000
Manager   Sneha 80000
Developer Arjun 60000

output:
Name:Rahul
Role:Developer
Bonus:10000.00




'''
class Employee:
    def __init__(self, n, s):
        self.name = n
        self.salary = float(s)

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.35

for _ in range(int(input())):
    role, name, salary = input().split()
    
    emp = Developer(name, salary) if role == "Developer" else Manager(name, salary)
    
    print(f"Name:{emp.name}")
    print(f"Role:{role}")
    print(f"Bonus:{emp.calculate_bonus():.2f}")