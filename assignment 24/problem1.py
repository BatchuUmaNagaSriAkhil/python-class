#Problem 1: Student Result Processor
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40


count = 0

try:
    with open("students.txt", "r") as file:
        for line in file:
            try:
                name, marks = line.strip().split(",")
                marks = int(marks)

                student = Student(name, marks)

                if student.is_pass():
                    count += 1

            except ValueError:
                continue

    print("Number of passed students:", count)

except FileNotFoundError:
    print("File Not Found")