'''
OOPS: Object Oriented Programming
programs are organized using objects
objects contain
1.data(variables)
2.behavior(functions/methods)

car ->object
student - >object

Each object here:
will have properties and actions
            |               |
            variables     Methods

Earlier the programming was written without loops

1. difficult to manage the large level projects
2.code duplication
3.less security
4.difficult maintenance

OOPs solve the above problems
1.classes
2.Objects
3.encapsulation
4.Inheritance
5.abstraction
6.polymorphism

'''
#Procedural programming
from msilib.schema import SelfReg
name = "Ramya"
marks = 30
def display():
    print(name,marks)

display()

#OOP approach:
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name,self.marks) 

s1 = Student("Akhil",95)    
s1.display()    

#data+functions --->
'''
advantages:
1.code reusability
2.better organization - modular and structure
3.security ->encapsulation
4.easy maintenance:update,debug
5.real world modelling
6.Scalability:large applications 


'''
'''
class: Blueprint of an object
collection of variables,methods?
Blueprint:
can be used to build many houses

'''
class ClassName:
    pass

'''
class:keyword creates class
classname:identifiers
pass:empty block

'''
#object : Instance of a class
            #or
#Actual memory representation of class            
class Student:
    pass

#create an object
obj = Student()
print(obj)
'''
obj -->instance name(object)
Student --> class name

'''
class Car:
    brand = "Audi"
    #Method
    #Self:Refers to the current object
    def start(self):
        print("Car started")
#create the objects 
c1 = Car()
c2 = Car()
c1.start()
c2.start()
print(c1.brand)
c1.brand#class -->obj searches
#for brand inside the class

#create a class names an employee
# create two variables company name and id
# create two methods to access name and company_name
# create two objects and access var and name  
class Employee:
    company_name = "TCS"
    id = "4407" 
    name = "Akhil"
    def display(self):
        print("hello",self.name) 
    def start(self):
        print("Company name: ",self.company_name)
e1 = Employee()
e2 = Employee()
e1.display()
e2.start()
print(e1.id)


'''
Constructor:  __init__ ()
special method
automatically called when an object is created
used to initialize the object data


'''
class Student:
    
    def __init__(self):
        print("Constructor is called")
        
s1 = Student()
s1.__init__
'''
Student()


object created

__init__automatically

if no constructor
manually assign the value

if yes
automatic initialization


'''
class Student:
    pass
s1 = Student()
s1.name = "ANAS"
s1.branch = "DS"        
        
#Example with constructor
class Student:
    def __init__(self):
        self.name = "ANAS"
        self.age = 21
    
obj1 = Student()
print(obj1.name)
print(obj1.age)

'''
self-->current object(obj1)
self-->obj1

#Constructor with parameters

'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
obj2 = Student("Anas",21)
print(obj2.name)
print(obj2.age)

'''
self -->obj2
name:"anas"
age:20

obj2______
name = "Anas"
age = 20


Step by step
1.object memory allocated
2.__init__ is called automatically
3.self points to object
4.variables initialized
5.object returned

'''
'''
#default Constructor

class Test:
def __init__(self)
    print("Default Constructor)
    
t = Test()

Parametrized constructor

class Test:
def __init__(self.x):
        self.x = 100

t = test()

Constructor                     |  Normal method
Automatically called            | Manually call it
Name fixed: __init__            | Any name
used for initialization         | used for operations
executes during object          | executes when called
creation

'''
class Student:
    def __init__(self):
        print("constructor")
#Normal method
    def display(self):
        print("Normal method")
c1 = Student()
c1.display()

'''
Instance Variables:

Variable that belong to an object
separate copy created for every object

They store:
    object-specific data
    
    Student  | Name  | Marks
    S1        Manish    98
    S2        Rajesh    99
    
each object stores it's own data

'''
class Student:
    def __init__(self,name,marks):
        #instance variables
        self.name = name
        self.marks = marks
        
s1 =Student("Anas",98)
s2 =Student("Lokesh",99)
s3 =Student("Akhil",100)
print(s1.marks)
print(s2.marks)
print(s3.marks)

'''
s1 object
---------
name = "Anas"
marks = 98

s2 object
---------
name = "Lokesh"
marks = 99

s3 object
---------
name = "Akhil"
marks = 100

Objects do not share instance variables


'''
#Instance methods
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
#Instance method
    def display(self):
        print(self.name)
        print(self.marks)
    
s1 = Student("Anas",98)
s1.display()
'''
s1.display()
#Dynamic object properties
adding the variables dynamically
after creating object

class Student:
    pass
    

'''
class Student:
    pass
s1 = Student()
s1.name = "Sai"
s1.age = 28
print(s1.name)

'''
Class variables:
'''
class Student:
    college_name = "CITY"
    def __init__(self,Branch):
        #Instance variable
        self.Branch = Branch

#Normal Method
def display(self):
    print(self.college_name)
    
s1 = Student("Cse")
s2 = Student("Csd")
print(s2.college_name)
print(s1.college_name)

'''

Self: refers to current object
            or
reference variable pointing to current object
'''
class Student:
    def display(Self):
        print("hello")
s1 = Student()
s1.display()
'''
s1.display()
    |
student.display(s1)
    |
self-s1(self points to s1)

'''
class Student:
    
    def show(self):
        print(self)
        
s1 = Student()
s2 = Student()
print(s1)
print(s2)

'''
        student class
        -------------
        College = CITY
        -------------
            |   |
            s1  s2
            
class Employee:
company = "Google"
def display(self):
    print(self.company)

e = Employee()
Two ways access:
print(e.company)

#No object use
print(Employee.company)
'''
'''
#class methods:
work with class variables
Operate on class level data

@classmethod - decorator

'''
#Basic example for class method

class Student:
    college = "CITY"

    @classmethod
    def show_college():
        print(cls.college)
    
Student.show_college
'''
@classmethod
decorator which tells python:
this method belongs to class not object

self --> current object
cls --> current class


'''
#Task: Create a class named as employee
#create one class variable
#use @classmethod to apply
# on method company_name
#print the company name
#using multiple objects
class Employee:
    company_name = "TCS"
    @classmethod
    def display(cls):
        print(cls.company_name)
e1 = Employee()
e2 = Employee()
e1.display()
e2.display()


'''
diff btw instance method and class method
instance method         |  class method
works on the object data| works on class data
uses self               | cls-current class
need object             | directly using class
access the instance var | access the class var


'''

class Student:
    college = "CIET"

    #instance method:refers object
    def instance_method(self):
        print("Instance method")
    
    #class method:refers class
    @classmethod
    def class_method(cls):
        print("Class Method")
s1 = Student()
s1.instance_method()
Student.class_method()
'''
Static method:
doesn't uses :object,class
they are:
utility/helper methods
not uses:
self,cls

Example:
add()
multiply()
@staticmethod-->decorator


'''
#static method example
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
print(Calculator.add(10,20))

class Message:
    @staticmethod
    def greet(name):
        print("Hello",name)
print(Message.greet("Anas"))


#create a class named as student
#create constructor
#class variable
#instance variable
#instance method
#class method
#static method
class Student1:
    college_name = "CITY"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
    @classmethod
    def show_college(cls):
        print("College Name:",cls.college_name)
    @staticmethod
    def greet():
        print("Welcome to OOPS")
s1 = Student1("Anas",21)
s1.display()
Student1.show_college()
Student1.greet()
