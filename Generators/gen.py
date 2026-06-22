'''
problem with list:
list = [1,2,3,4,5]
entire list is stored in memory
nums = [i for i in range(100000)]
python consumes:
high memory
slower

Generator:
produces values one at a time only when it is needed saves memory




'''
#Example:
def numbers():
    yield 1
    yield 2
    yield 3
x = numbers()
print(x)  

#access the numbers
print(next(x))
print(next(x))

'''
1.first next()
yield 1 ->1
function paused

2.second next()
resume from previous position
yield 2 --> 2
function pause

3.third next()
resume from previous position
yield 3 --> 3
pause again 

Generators:
remembers the variables
remember line position
continue from the same place

# diff between return and yield
return                      yield
ends the function           pauses the function
returns single value by 1   will return multiple values
no state memory             remembers the state
'''
def test():
    yield 1
    yield 2
x = test()
print(next(x)) 
print(next(x)) 

def test():
    yield 1
    yield 2
for i in test():
    print(i)

def Evennumbers(limit):
    num = 2
    while num <= limit:
        yield num
        num +=2
x = Evennumbers(10)
for i in x:
    print(i)

'''
#lazy evaluation

values are generated when needed
generators are lazy

''' 
#write a program for fibonacci using generators 
def fibonacci(limit):
    a, b = 0, 1
    while a<=limit:
        yield a
        a, b = b, a + b
x = fibonacci(6)
for num in x:
    print(num)  