'''
Password Manager:
Create a class PasswordManager:
Rules:
1.minimum 8 characters
2.one uppercase
3.one lowercase
4.one digit

if invalid
weak password
else:
Password Set Successfully

'''
class PasswordManager:
    def __init__(self):
        self.__password = ""

    def set_password(self, password):
        if len(password) < 8:
            print("weak password")
            return

        upper = False
        lower = False
        digit = False

        for ch in password:
            if 'A' <= ch <= 'Z':
                upper = True
            elif 'a' <= ch <= 'z':
                lower = True
            elif '0' <= ch <= '9':
                digit = True

        if upper and lower and digit:
            self.__password = password
            print("Password Set Successfully")
        else:
            print("weak password")

    def get_password(self):
        return self.__password


pm = PasswordManager()
pwd = input("Enter Password: ")
pm.set_password(pwd)