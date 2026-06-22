'''
Login Authentication System
A company wants to store user credentials
write a program:
1.Take the input from the user
2.login using users into users.txt
3.validate the credentials from file
4.handle  invalid login attempts

'''
class LoginSystem:
    def register(self):
        username = input("Enter the username:")
        password = input("Enter the password:")
        with open("users.txt","a") as file:
            file.write(
                username + " " +password+"\n"
            )
        print("Registration Successful")
    def Login(self):
        try:
            username = input("Enter the Username:")
            password = input("Enter the Password:")
            found = False
            with open ("users.txt","r") as file:
                for line in file:
                    u,p = line.strip().split()
                    if (username == u and password == p):
                        found = True
                        break
                    if found:
                        print("Login Successful")
                    else:
                        print("Invalid Credentials")
        except FileNotFoundError as e:
            print(e)

obj = LoginSystem()
obj.register()
obj.Login()