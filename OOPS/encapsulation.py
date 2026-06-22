'''
What is encapsulation?
Binding data and methods together into a single unit

And:
restricting direct access to data

Encapsulation protects the data from
1.Unauthorized access
2.accidental modifications

Similarly In OOPS:
Data is hidden inside the class
and accessed using methods

Key idea
Data + Methods
    |
Combined into a single unit
    |
Controlled Access

Features of Encapsulation:
1.Security
2.Data Hiding
3.Controlled Access
4.Better Organization

'''
#No Encapsulation
#from Homework.fourth import amount
balance = 50000

balance = -50000

#Encapsulation
class Bank:
    def __init__(self):
        self.balance = 10000
    def deposit(self,amount):
        self.balance +=amount
        
    def show_balance(self):
        print(self.balance)
        
b1 = Bank()
b1.deposit(5000)
b1.show_balance()  #data and methods are bound together

#data hiding
#restricting access to direct variables

'''
Goal: To prevent the data modifications
and misuses of data

Access modifiers in python:
1.Public:default
2.Protected: _single_underscore
3.Private: __double__underscore

'''
#1.Public: Members can be accessible everywhere
#default access type in python

class Student:
    def __init__(self):
        self.name = "Anas"
        
s1 = Student()
print(s1.name)
'''
Accessed anywhere
No restriction
Default behaviour
'''

#2.Protected: _single_underscore
#should not be accessed directly outside class

class Student1:
    
    def __init__(self):
        self._marks = 90
        
s1 = Student1()
print(s1._marks)

'''
Python protected members are not exactly protected

_marks: Protected by convention

Please dont access it directly

where to use?
1.During inheritance
2.for internal usage

'''
'''
#3.Private: __double__underscore

used for : strong data hiding
'''
class Student2:
    def __init__(self):
        self.__marks = 99
        
s1 = Student2()
#print(s1.__marks)

#Name Mangling

# __marks
#   |
#_Student__marks

'''
Prevent:
Accidental direct access
Accidental Overriding

'''
#can i access private var inside the class

class Student3:
    def __init__(self):
        self.__marks = 91
        
    def show(self):
        print(self.__marks)
        
s1 = Student3()
s1.show()

#Try to access using name mangling

class employee:
    def __init__(self):
        self.__salary = 50000
e1 = employee()
#Iam using name mangling to access 
print(e1._employee__salary)

'''
self.__marks
    |
Python will convert
    |
self._Student__marks
'''
'''
Access Modifiers  | Syntax   | Accessible outside
1.Public            Variable    Yes
2.Protected        _Variable    yes(convention only)
3.Private          __variable   no directly

#Task:
create a class named "BankAccount"
#balance --> Private
#deposit
#withdraw amount
#check for balance
#print balance using name mangling

'''
class Bankaccount:
    def __init__(self):
        self.__balance = 10000
        
    def deposit(self,amount):
        self.__balance += amount
        
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            
    def check_balance(self):
        print("Balance:",self.__balance)
b1 = Bankaccount()
b1.deposit(10000)
b1.withdraw(9230)
b1.deposit(5000)
b1.withdraw(12000)
b1.check_balance()

'''
Getters and setters:
getters -- read the data
setters -- modify/update the data

#why use?

student.marks = -90
No Validation
'''
#without getters and setters
class Student4:
    def __init__(self):
        self.marks = 90
        
s1 = Student4()
s1.marks = -50
print(s1.marks)

#Using getters and setters
class Student5:
    def __init__(self):
        self.__marks = 90
        
    #getter method
    def get_marks(self):
        return self.__marks
    #setter method
    def set_marks(self,value):
        if value >= 0:
            self.__marks = value
        else:
            print("Invalid marks")
            
b1 = Student5()
print(b1.get_marks())
b1.set_marks(95)
print(b1.get_marks())
b1.set_marks(-95)
print(b1.get_marks())

#task:create a class BankAccount
#create getter for returning balance
#create setter for updating balance
#amount >= 0
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = 0
        self.set_balance(balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

acc = BankAccount(1500)

print("Balance:", acc.get_balance())

acc.set_balance(1000)
print("Updated Balance:", acc.get_balance())

acc.set_balance(-200) 
print("Final Balance:", acc.get_balance())

class Student6:
    def __init__(self):
        self.__marks = 90
        
    #getters
    @property
    def marks(self):
        return self.__marks
    #setter
    @marks.setter
    def marks(self,value):
        if value >= 0:
            self.__marks = value
        else:
            print("Invalid marks")
        
s1 = Student6()
print(s1.marks)
s1.marks = 95
print(s1.marks)
