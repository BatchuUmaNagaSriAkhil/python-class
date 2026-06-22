'''         
            logic for password verifier
                       store the original password
                                 |
                        ask the user for input
                                 |
                compare the entered password with the original password
                                 |
                        if wrong:
                             show error message
                             try again 
                                 |
                        if correct:
                        stop loop
                        login successful                    
'''
original_password = "123456"
while True:
    entered_password = input("Enter the password: ")
    if entered_password == original_password:
        print("Login successful!")
        break
    else:
        print("Incorrect password. Please try again.")
