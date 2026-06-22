'''
Problem 1 — Student Information System
Problem Statement
Create a class 
Student to store and display student details.
Requirements
▪ 
▪ 
▪ 
Create instance variables: 
name , 
roll_no , 
Use constructor to initialize values.
Create an instance method 
marks
▪ 
display_details() to print student details.
Create another instance method 
is_passed() : 
▪ 
▪ 
return 
"Passed" if marks >= 35
otherwise return 
"Failed"

'''
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def is_passed(self):
        return "Passed" if self.marks >= 35 else "Failed"


name = input()
roll_no = int(input())
marks = int(input())

s = Student(name, roll_no, marks)
s.display_details()
print(s.is_passed())