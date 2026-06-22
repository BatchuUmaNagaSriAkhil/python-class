#Problem statement:

#Take 3 sides from user and check
#whether triangle is
#1.Isosceles --> two sides are equal
#2.Equilateral --> all sides are equal
#3.Scalene --> 3 different sides
A = int(input("Enter the first side: "))
B = int(input("Enter the second side: "))   
C = int(input("Enter the third side: "))
if A == B == C:
    print("Equilateral triangle")
elif A == B or B == C or A == C:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    

