# Problem 10: Loan Approval System
# A bank approves loan if: Age between 21 and 60; Salary ≥ ₹25,000; Credit score
# ≥ 700. Extra conditions: Salary > ₹50,000 and credit score > 800 → Premium
# loan; Existing loans more than 2 → Reject.
# Concepts: Logical operators, Nested if statements, Comparison operators
# Sample Input:
# Age: 30
# Salary: 60000
# Credit Score: 820
# Existing Loans: 1
# Sample Output:
# Premium Loan Approved

# Source Code:

age = int(input("Age: "))
salary = float(input("Salary: "))
credit_score = float(input("Credit Score: "))
existing_loans = int(input("Existing Loans: "))

if 21 <= age <= 60 and salary >= 25000 and credit_score >= 700:
    if salary > 50000 and credit_score > 800:
        print("Premium Loan Approved")
    else:
        print("Regular Loan Approved")
else:
    print("Loan Rejected")
