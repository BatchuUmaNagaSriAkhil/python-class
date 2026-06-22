'''
Decoraters:
adds the extra functionality to the function without changing the original function
Gift wrapper:
wrapper adds:
extra layer,beauty

decorator = weapper around the function
why decoraters are needed?
logging:
authentication, 
timing,
validation

if no decoraters
1.repeated code
2.messy programs

#In python --- functions are treated like variables
'''
def greet():
    print("Hello students")
x = greet 
x()    
#nested functions:
def outer():
    def inner():
        print("Inner side")
    inner()
outer()  

#returning the function
def outer():
    def inner():
        print("Inner side")
    return inner()
x = outer
x()  

#simple decorater
def decorator_function(original_function):
    def wrapper():
        print("Before function call")
        original_function()
        print("After function call")
    return wrapper

#original Function:
def greet():
    print("Hello Students")

#apply manually
decorated = decorator_function(greet) 
decorated()   
'''
greet()
|
decorated_function()
|
wrapper created()
|
extra functionality is added

special symbol : @

'''
@decorator_function
def greet():
    print("Hello Students")

#Example2:
def smart_divide (func):
    def wrapper():
        print("Checking before div")
        func()
        print("Division complete")  
    return wrapper    
@smart_divide
def divide():
    print(10/2) 

divide()   

#Example3:

def decorator_function(original_function):
    def wrapper(name):
        print("Before function call")
        original_function(name)
        print("After function call")
    return wrapper
@decorator_function
def greet(name):
    print("hello",name)

greet("akhil")    

#time decorator
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time", end -start)
    return wrapper
@timer  
def test():
    for i in range(10000):
        pass

test()    

#example2:
def login_required(func):
    def wrapper():
        print("Checking the user login")
        func()
    return wrapper
@login_required
def dashboard():
    print("Welcome to dashboard")

dashboard()
