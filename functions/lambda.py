'''
Lamda Function; it is a small and anonyymous 
#function without name
#defined using lamda
can pass any number of arguments
can onnly have one expression
returns the value automatically

normal function:

deff add(a,b):
return a+b

add(10,20)

#write using lambda

add = lambda a,b:a+b

#calling the function
add(10,20)

'''
#Task:write a normal funct to square of num
#convert normal function to lambda function

square = lambda n: n * n

print(square(5))

'''
arr = list(map(int, input().split()))

#map(): applies the function each
#element of iterable
map(function,iterable)

example:
def square(x):
    return x*x

nums = [1,2,3,4]
result = list(map(square,nims))
print(result)

'''
def square(x):
    return x*x

nums = [1,2,3,4]
result = list(map(square,nums))
print(result)


#Task:Given a list of numbers
#Convert each number into cubesusing map and lambda
def square(x):
    return x*x

nums = [1,2,3,4]
result = list(map(lambda x:x*x,nums))
print(result)
'''
#what is filter?
selects the elements based upon the condition

syntax:
filter(function,iterable)

Example:
def is_even(x):
    return x%2==0

list = [1,2,3,4,5]
result = filter(is_even,list)
print(result)



'''
'''
def is_even(x):
    return x%2==0

list = [1,2,3,4,5]
result = filter(is_even,list)
print(result)
'''

#task: given with a list with friends names
#filter the names letter starting with A
# by using filter and lambda 

friends = ["Anas", "Bala Bhavadeep", "Akhil", "Venu", "Varfan", "Lokesh", "Kowshik"]

result = list(filter(lambda x: x.startswith("V"), friends))

print(result)

'''
what is reduce()?
Repeatedly applies function
Reduces the iterable to single value

syntax:

reduce(function,iterable)


'''
#function tools ---> module

from functools import reduce

nums = [1,2,3,4,5]
result = reduce(lambda a,b:a+b,nums)
print(result)