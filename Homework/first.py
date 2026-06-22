# Problem 1: Smart Salary Bonus Checker
# A company gives bonuses based on employee salary and experience. Rules: If
# experience is greater than or equal to 5 years: Salary below 30,000 → 20%
# bonus; Salary between 30,000 and 50,000 → 15% bonus; Salary above 50,000 →
# 10% bonus. Otherwise: Flat 5% bonus. Display the bonus amount and final
# salary.
# Concepts: Variables, Typecasting, Nested conditions, Arithmetic operators
# Sample Input:
# Enter salary: 45000
# Enter experience: 6
# Sample Output:
# Bonus = 6750.0
# Final Salary = 51750.0
# Problem 2: Electricity

#Source Code:
# Problem 1: Smart Salary Bonus Checker
salary = float(input("Enter salary: "))
experience = int(input("Enter experience:"))

if experience >= 5:
    if salary < 30000:
        bonus = salary *(20/100)
    elif salary >= 30000 and salary <= 50000:
        bonus = salary * (15/100)
    elif salary > 50000:
        bonus = salary * (10/100)
else:
    bonus = salary * (5/100)

final_salary = salary + bonus
print("Bonus =", bonus)
print("Final Salary =", final_salary)