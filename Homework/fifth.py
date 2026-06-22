# Problem 5: Login System with Security Check
# Create a login system. Conditions: Username and password must match; If
# password length is less than 8 → weak password warning; If login fails 3 times →
# account blocked.
# Concepts: Variables, Logical operators, Nested conditions, Counters
# Sample Output:
# Login Successful OR Account Blocked

# Source Code:

correct_user = "admin"
correct_pass = "password123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == correct_user and password == correct_pass:
        if len(password) < 8:
            print("Login Successful")
            print("Warning: Weak password")
        else:
            print("Login Successful")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Login Failed. Attempts left: {remaining}")
        else:
            print("Account Blocked")

# Concepts: logical 'and', nested if, counter variable 'attempts'