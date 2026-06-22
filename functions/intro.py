'''
what is function?
Function is a block of reusable code .performs specific task.


why function?
1.Avoid repetition
2.Improves readability
3.Easy Debug
4.Modular programming

#function definition

def function_name(Parameters):
    """Doc strings"""
    statements
    return value

    def --> keyword
    function_name --> identifiers
    parameters --> inputs
    return --> output

#Function calling : executing the code
function_name()

                            functions are 2 types
                                /           \
                        built in function   user defined function

BuiltIn functions: which are already defined
Example:input()
print()
mean()
sum()
max()
User Defined functions:we will create our logic as per our requirement


'''
#create a function
def hello():
    print("Hello World")
#call the function
hello()

#parameters: variable passed during the function definition

def add(a,b):
    print(a+b)
    return a+b

#arguments = values passed during function call
#calling the function
add(2,3)  #2,3 -- arguments

'''
Types of arguments:
1.Positional arguments:
arguments passed in order

'''
#Example:
def multiply(a,b):
    print(a*b)
    return a*b

#call the function
multiply(2,3)

#Task: Create a function to calculate
#simple interest using positional args

def interest(p, r, t):
    return (p * r * t) / 100

print(interest(100, 5, 2))

#2. keyword arguments:
def sub(a,b):
    print(a-b)
    return a-b

sub(b=5,a=20)#No order

#Task:call the simple interest function
#using keyword arguments

def interest(p, r, t):
    print(interest)
    return (p * r * t) / 100


print(interest(p=100, r=5, t=2))

#3. Default arguments : used when value is not provided
#example
'''
def student(name ="Anas"):
    print(f"student name is {name}")
student("Anas")

'''
def student(name,branch= "DS"):
    print(f"student name is {name} and branch is {branch}")
student("Anas")

#Task: create a function to calculate squares of default parameters

def square(a=5):
    square = a**2
    print(square)
square(5)

#4. variable length arguments
def total (*args):
    print(args)
    print(sum(args))
    print(max(args))

#call the function
total(10,20,30,40)

#Task: Create a function to find sum of any number of values
def total(*value):
    print(sum(value))

total(10,20,30,40,50,60,70,80,90,100)


'''
#kwargs --> keyword arguments

def student_details(**kwargs):
    print(kwargs)


'''
def student_details(**kwargs):
    print(kwargs)

student_details(name="ANAS",branch="DS",roll="91")

#task: create a function to print employee details using kwargs

def employee_details(**kwargs):
    print(kwargs)

employee_details(name="Lokesh",company="TCS",salary="25000")

#Task: write args and kwargs together in a function

def details (*args,**kwargs):
    print(args)
    print(kwargs)

details(10,20,30,name="Anas",salary="30,000",experience="2yeras",company="JP Morgan Chase & Co")

'''

return statement: send the value back to the caller

def add(a,b)
return a+b

result = add(10,20)
print(result)


print                   |   return
display the output          sends the value
cannot reuse                can be reused

Multiple return values:
def calculate(a,b):
    return a+b,a-b,a/b

    format = tuple

s,sub,div = calculate(20,30)



'''
def calculate(a,b):
    return a+b,a-b,a/b

    format = tuple

s,sub,div = calculate(20,30)
print(s,sub,div)

#Task: create a function that returns multiple values
#1.Min,2.Max,3.Average of the numbers

def values(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

print(values([10, 20, 30, 40, 50]))

'''
#function doc strings

doc string describes:
1.what function does
2.parameters
3.return value

def add(a,b):
"""This function add two numbers and returns result"""
return a+b



'''
def add(a,b):
    """This function add two numbers 
    and returns result"""
    return a+b

print(add.__doc__)
print(help(add))

#Task:write a docstring for 
# the simple interest program

def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest.__doc__)
help(simple_interest)


'''
variable scopes:
1.local scope:
variables declared inside the function
def test ():
    x = 100
    print(x)
test()
2.global scope:
variables declared outside the function
def show():
    x = 200
    print(x)
show()




'''
def test ():
    x = 100
    print(x)
test()

def show():
    x = 200
    print(x)
show()

x = 0

def update():
    global x
    x= x+5

update()
print(x)

#Task: Try without using global and tell me error
x = 0

def update():
    x= x+5

print(x)

'''
Task:
create a function bank_transaction()
which accepts:
1.account holder(string)
2.balance
3.transaction_type(deposit/withdraw)
4.amount

by using:
1.default arguments
return statements
global balance

'''
balance = 0 

def bank_transaction(holder, amount, t_type="deposit"):
    global balance
    if t_type == "deposit":
        balance += amount
    else:
        balance -= amount if amount <= balance else 0
    return holder, balance

print(bank_transaction("Varfan", 1000))
print(bank_transaction("Varfan", 300,"withdraw"))
print(bank_transaction("Varfan", 2000))
print(bank_transaction("Varfan", 600,"withdraw"))
print(bank_transaction("Varfan", 2000,"withdraw"))
print(bank_transaction("Varfan", 49.50,"withdraw"))

