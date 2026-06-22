'''
Iterators:
Gives one element at a time on demand

Python refers iterators:
memory efficiency controlled access

Iterabe:is an object can be looped
1.list
2.tuple
3.set
4.dict
5.string

Examples:
nums = [10,20,30,40]

for x in nums:
    print(x)

#Syntax:
iterable_object = [1,2,3,4]
it = iter(iterable_object)    
print(it)
'''
iterable_object = [1,2,3,4]
it = iter(iterable_object)    
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''
list
 |
iter()
 |
Iterator

how loop in python works internally
Iterators --will be used internally
iter(),next()

nums = [1,2,3,4]

for x in nums:
    print(x)
it = iter(nums)
while true:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break    
'''
nums = [1,2,3,4]
it = iter(nums)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break  

'''
nums = [2,3,4]
it = iter(nums)
print(next(it))
'''
name = "python"
it = iter(name)
print(it)

t = (1,2,3)
it = iter(t)
print(it)

d = {"a":10,"b":20}
it = iter(d)
print(it)
print(next(it))
print(next(it))

#no iterator
nums =[i for i in range(1000000)]
#huge memory
#iterator approach
nums = iter(range(1000000))
#only the current element will be processed

#create a custom iterator
#count
class count:
    #construct
    def __init__(self,limit):
    
        self.num = 1
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.num>self.limit:
            raise StopIteration
        x = self.num    
        self.num += 1
        return x
#object creation    
c = count(5)  
for i in c:
    print(i)

class EvenNumbers:
    def __init__(self,limit):
        self.num = 2
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.num>self.limit:
            raise StopIteration
        x = self.num
        self.num +=2
        return x
    
c = EvenNumbers(5)  
for i in c:
    print(i)
                