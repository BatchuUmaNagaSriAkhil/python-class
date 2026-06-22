'''
Module:
a module is simply a python file containing code

why?
1.large file
2.hard to maintain
3.difficult to reuse

modules:
Reusability
Organization
Readability
Collaboration
'''
import calculator

print(calculator.add(1,2))
print(calculator.sub(19,18))

#Task: create a module named as gretting

import greeting

greet1 = greeting.greet()
print(greet1)

greet = greeting.greet2()
print(greet)

import math
print(math.sqrt(33))
print(math.factorial(5))

import random
print(random.choice("Anas"))

#math and power
from math import sqrt,pow
sqrt(3)
pow(2,2)

import math,random

#to get all the attributes from math
from math import * 

#from Looping import new
#new.hello()

#collection of modules is called package

import datetime as dt
print(dt.datetime.now())

'''
Module          meaning
1.math          Mathematics
2.random        Random values
3.datetime      Date & Time
4.os            Operating System
5
'''
#help("modules")
'''
#Package:
it is a folder containing multiple modules

School/ --> package
    student.py
    teacher.py
    management.py
    

main.py --> from school import student

__init__.py
Purpose:
it is a special file used to identify package
1.marks directory as package
2.Runs initialization code
3.controls the import

'''
#importing from package
#from school.student import show_student
#show_student()

#builtin methods
import math
#round upward
print(math.ceil(5.2))
#round downward
print(math.floor(5.2))

#constants
print(math.pi)
print(math.e)

#Task:Area of a circle
import math
r = 5
print("Area =", math.pi * r**2)

#random builtin methods
#used for random values


import random

#randunt()
print(random.randint(1,100))

#choice()
fruits = ["Apple","Banana","Orange"]
print(random.choice(fruits))

#random()
print(random.random())

#shuffle()
cards = [1,2,3,4]
random.shuffle(cards)
print(cards)

#Task: Build the dice simulator
import math
print(random.randint(1,6))

#Date?
import datetime
print(datetime.date.today())

#custom date
d = datetime.date(2005,12,19)
print(d)

#Build the age calculator
import datetime
birth_year = 2005
current_year = datetime.date.today().year
print(current_year-birth_year)

import os
print(os.getcwd())

#mkdir --make directory
#print(os.mkdir("PythonClass"))

#change the name(rename)
#os.rename("PythonClass","2027Batch")

#listdir()
print(os.listdir())

#remove directory
#os.rmdir("2027Batch")

#Task: Display all the file in a dir

import os
files = os.listdir()
for file in files:
    print(file)

#module - sys
#provides the information about
#python interpreter
import sys
print(sys.version)

print(sys.exit())
print(sys.path())