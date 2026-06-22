#Problem 1 — Smart Login Attempt Tracker
class InvalidUsernameError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class ShortUsernameError(Exception):
    pass


class LoginSystem:

    def __init__(self, users):
        self.users = users

    def login(self, username):

        if len(username) < 4:
            raise ShortUsernameError(
                "ShortUsernameError: Username must be at least 4 characters."
            )

        if not username.isalpha():
            raise InvalidUsernameError(
                "InvalidUsernameError: Username must contain only alphabets."
            )

        valid = False

        for i in self.users:
            if i.lower() == username.lower():
                valid = True
                break

        if not valid:
            raise UserNotFoundError(
                "UserNotFoundError: Username not found."
            )

        print("Login Successful")


n = int(input())

users = []

for i in range(n):
    users.append(input())

username = input()

obj = LoginSystem(users)

try:
    obj.login(username)

except Exception as e:
    print(e)