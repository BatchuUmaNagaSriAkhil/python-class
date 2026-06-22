#write a program to check whether the given year is leap year or not
#Conditions:
#1.divisible by 400
#2.divisible by 4 
#3.but not by 100
year = int(input("Enter the year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")
    