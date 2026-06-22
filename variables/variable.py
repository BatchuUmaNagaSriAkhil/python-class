# x = 100
# print(x)

# _name = "Tejesh"
# print(_name)

# # 2name: should not start with a number
# # name@123: should not contain special characters except underscore

# age = 20
# Age = 30# age and Age are different variables because of case sensitivity
# print(Age)

# # if : keywords cannot be used as variable names

# #first-name = "Tejesh" # should not contain hyphen

# a = input("Enter the value: ")
# b = input("Enter the value: ")  
# print(a+b) # by default input is of string type, so it will concatenate the two inputs  
# type(a) # by default input is of string type

# #Typecasting: converting one data type to another
# x = int(input("Enter the value of x: ")) # typecasting input to integer.
# y = int(input("Enter the value of y: "))
# print(x+y) # now it will add the two inputs as they are of integer type     

# #write a program to greet the user by taking input from the user
# name = input("Enter your name: ")
# print("Hello ", name , "! Welcome to Python Progamming.")

# #string --> float
# price = float(input("enter your price:"))
# print(type(price))

# #int --> string
# x = str(100)
# print(type(x))

# write a program to perform avg of the numbers(3)
#num1 = float(input("Enter the number:"))
#num2 = float(input("Enter the number:"))
#num3 = float(input("Enter the number:"))
#avg = (num1 + num2 + num3)/3
#print("The average is: ", avg)

n = input()
vowels = "aeiouAEIOU"
v = 0
c = 0
for i in n:
    if i.isalpha():
        if i in vowels:
            v +=1
        else:
            c +=1
if v == c :
    print("Balanced")
else:
    print("not balanced")                
