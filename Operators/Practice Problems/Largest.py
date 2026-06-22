#Largest of 4 numbers
#1.logical operators and conditionals
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
if a > b and c and d:
    print("The largest number is: ", a)
elif b > c and d:
    print("The largest number is: ", b)
elif c > d:
    print("The largest number is: ", c)
else:
    print("The largest number is: ", d)
    
    
#Task : write the pseudocode for above code

'''
START


Input a, b, c, d

IF a is greatest
    Display a
ELSE IF b is greatest
    Display b
ELSE IF c is greatest
    Display c
ELSE
    Display d

END

'''

#Truthly and Falsy statements
if 0:
    print("hello")
    
#It will not execute

#Short circuit evaluation

if True or 10/0:
    print("safe")
    
#No  -error and prints safe

if True:
    print("hello")