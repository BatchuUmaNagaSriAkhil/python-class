#Take the username
username = input("Enter your username: ")

#First Condition
if username == "admin":
    password = input("Enter your password: ")

    #Nested condition
    if password == "1234":
        print("Login successful!")
    else:
        print("wrong password")
        
else:
    print("invalid username")        