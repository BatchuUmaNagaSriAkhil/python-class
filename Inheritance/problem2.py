'''
Problem2:
Student and college
class variable --> college name
create a child class student
instance variables -->student _name

display:
1.college_name
2.student_name

'''
class College:
    college_name = "CIET"
class Student(College):
    def __init__(self,name):
        self.student_name = name
s1 = Student("Anas")
print(s1.college_name)
print(s1.student_name)
