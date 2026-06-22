# Problem 3: Student Scholarship Eligibility
# A student gets scholarship if: Attendance ≥ 85% AND Marks ≥ 75. Extra
# condition: If family income is below ₹2,00,000 → Full scholarship; Otherwise →
# Partial scholarship. Else student is not eligible.
# Concepts: Logical operators, Nested conditions, Comparison operators
# Sample Input:
# Attendance: 90
# Marks: 80
# Income: 150000
# Sample Output:
# Eligible for Full Scholarship

#Source Code:

attendance = int(input("Attendance: "))
marks = int(input("Marks: "))
income = int(input("Income: "))

if attendance >= 85 and marks >= 75:
    if income < 200000:
        print("Eligible for Full Scholarship")
    else:
        print("Eligible for Partial Scholarship")
else:
    print("Not Eligible")