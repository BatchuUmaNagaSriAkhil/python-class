#Problem 3: Employee Directory Search
class EmployeeDirectory:
    def __init__(self):
        self.employees = []

    def load_data(self):
        file = open("employees.txt", "r")

        for line in file:
            self.employees.append(line.strip())

        file.close()

    def search_by_letter(self, ch):
        found = False

        for emp in self.employees:
            if emp.startswith(ch):
                print(emp)
                found = True

        if not found:
            print("No Match")


try:
    directory = EmployeeDirectory()

    directory.load_data()

    ch = input()

    if len(ch) != 1 or not ch.isalpha():
        print("Invalid Input")

    else:
        directory.search_by_letter(ch)

except FileNotFoundError:
    print("File Not Found")