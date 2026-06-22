'''
Student marks valuator
Create a class student:
requirements:
Private Var --> __marks
method set_marks(marks)
method get_marks(marks)

rules:
marks must be btw 0-100
otherwise:
 print("invalid")

input [85] --> 85
otherwise:
print("invalid")
'''
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("invalid")

    def get_marks(self):
        return self.__marks

s = Student()
marks = int(input())
s.set_marks(marks)
if 0 <= marks <= 100:
    print(s.get_marks())