'''
what is a loop?

a loop is used 








'''
# #Looping ---2 types
#    /      \
#    For    While

'''for --> used when num of iterations is known
    while --> used when num of iterations is not known

    Benefits:
    1. Reduces the code duplication and complexities
    
    Execution flow of loops

            start
            
    
            condition'''

#Task: Multiplication table of 5 using for loop
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
    
#Task: sum of numbers(1,6) 1+2+3+4+5 ->15
total = 0
for i in range(1, 6):
    total += i
print(f"Sum of numbers from 1 to 5 is: {total}")


#Task: s = "Akhil" now count char in your name using for loop
s = "Akhil"
count = 0
for char in s:
    count += 1
print(f"Number of characters in the name is: {count}")


#using for loop and print only
#even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)        
        
#sum of numbers --using while 
#do sum until the input is 0
#total = 0
#num = int(input("Enter a number (0 to stop): "))
#while loop
#i =1 
#while i<=5:
#    print(i)
 #   i += 1
#infinite loop
#while True:
    #print("run forever")

num = int(input("Enter a number (0 to stop): ")) 
total = 0
while num !=0:
    total +=  num
    num = int(input("enter a number (0 to stop): ")) 
print(total)
   