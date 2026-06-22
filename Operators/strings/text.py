'''
Strings : one of the most important topic

Strings are the sequence of characters:
Enclosed in  --> single quotes ' '
                --> double quotes " "
                --> triple quotes '''  '''
                                            Mutability
                                           /          \
                                        Mutable     Immutable
                                            |            |
                                        change      non-change

Example:
                                          
name = "Akhil"
name[0] = "a"  # TypeError: 'str' object does not support item assignment

#Memory space
str = "S T R I N G "
    =  0 1 2 3 4 5 
    '''
name = "A k h i l Batchu"
print(name)
print(name[0])
print(name[0:3])
str = "College"
print(len(str))
#Slicing:
#str[start,end,step]
print(str[0:3:1])
#converting negavtive index to positive index:
print(str[-1:-4:-1])
print(str[6:3:-1])
#ommiting start
print(str[:3])
print(str[3:])
#step slicing:
print(str[0:6:1])
print(str[0:6:2])
#Reverse string:
print(str[::-1])
'''
#string traversal:

names = "Chalapathi"

for i in names:
    print(i))
for i in range(len(names)):
    print(names(i))



'''
names = "Chalapathi"

for i in names:
    print(i)
    print()
for i in range(len(names)):
    print(names[i]) 
for ch in range(len(names)):
    print(ch,names[ch])
print (names.upper())#all letteres will get into captial letters
print(names.lower())#all letteres will get into small letters
print(names.capitalize()) #first letter will be in captial
print(names.title())#first letter will be in captial
college = " chalapathi "
print(college.strip()) #used to remove the gaps in word
#Replace

text = "I love my self"
print(text)
replaced_text = text.replace("love","like")
print(replaced_text)
fruit = "banana"

#to count the frequency of "a"

print(fruit.count("a"))

#startswith 

print(names.startswith("C"))

#endswith

print(names.endswith("hi"))

#split()
texts = "Python  C  Java"
print(texts.split())

#use join 
#python-c-java
seperated = texts.split()
print(type(seperated))
print("-".join(seperated))
#Searching inside the strings

new = ("-".join(seperated))
print(new)
#find()  -->

print(new.find("Python"))
#Using membership operator

print("Python" in new)

#index()
print(new.index("t"))

#which is safe find() or index()?
#find() is safe to use beacuse it is getting error in index function

#string formatting
name = "akhil"
age = 20
#F - strings
print(f"my name is {name} and my age is {age}")
#old college mehod
print("Name:",name,"and age is:", age)

#format()
print("welcome {}".format(name))
#Escaping charaters or sequence
print("hello \n world")
print("hello \t world")
print("hello \n\t world")
#R - strings (Regex - regular expression)
path = r"c:/donwloads/photos/pic.jpeg" #r --> tells you interpreter that there are no escaping characters in path

#swapcase() ---?
print(texts.swapcase())

#casefold() ---> stronger lower conversion
print(texts.casefold())

#center -- >
print(texts.center(100))

