# Problem 9: Mobile Password Strength Checker
# Check whether a password is: Weak, Medium, Strong. Rules: Length less than 6
# → Weak; Length between 6 and 10: Must contain digits and alphabets →
# Medium; Greater than 10: Must contain uppercase, lowercase, digits, special
# characters → Strong.
# Concepts: Variables, Logical expressions, Nested conditions, String basics
# Sample Input:
# Enter password: Python@123
# Sample Output:
# Strong Password

# Source Code:

password = input("Enter password: ")  

if len(password) < 6:
    print("Weak Password")
elif len(password) <= 10 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("Medium Password")
elif len(password) > 10 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()-+" for char in password):
    print("Strong Password")
else:
    print("Invalid Password")
