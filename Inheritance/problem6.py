'''
Online course Access System
An online learning platform provides 
different levels of course access
create a parent class Course: with
-> Student_name 
create a method:
access_level():
Then create two child classes 
->FreeCourse
Access Level = "Limited Access"
->Premium Course 
Acess Level = "Full ACcess"
write a program:
1.Accept student details 
2.Create objects using inheritance 
3.Print Student access information

input:course_type,student_name

sample:
4
Free Amit
Premium Neha
Free Rohan
Premium Rakesh

output:
Student:Amit
Course_type:Free
Access:Limited Access
'''
class Course:
    def __init__(self, student_name):
        self.student_name = student_name

    def access_level(self):
        pass


class FreeCourse(Course):
    def access_level(self):
        return "Limited Access"


class PremiumCourse(Course):
    def access_level(self):
        return "Full Access"


n = int(input())

for _ in range(n):
    course_type, student_name = input().split()

    if course_type == "Free":
        student = FreeCourse(student_name)
    else:
        student = PremiumCourse(student_name)

    print(f"Student:{student.student_name}")
    print(f"Course_type:{course_type}")
    print(f"Access:{student.access_level()}")