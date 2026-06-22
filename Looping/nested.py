'''
nested loop: loop innside the loop
first loop: outer loop ---> row
second loop: inner loop ---> column

Example:
i = 1
while i <= 3:
    j = 1 
    while j <= 2:
        print(i,j)
        j += 1
    i += 1

for loop:
for outer in range():
    for inner in range():
    #code
for every row:
    for every student in that row:
        #greet the student

How nested loop works using for loop:
for i in range(1, 4):
    for j in range(1, 3):
        print(i,j)

Why nested loops are used?
1.Pattern problems
2.Matrix problems
3.Tables
4.Games
5.Grid system
6.Comparing the elements



'''
i = 1 #outer loop
while i <= 3:
    j = 1 #inner loop
    while j <= 2:
        print(i,j)
        j += 1
    i += 1 

for i in range(1, 4):
    for j in range(1, 3):
        print(i,j)

#print the pattern of stars
for i in range(1, 5):
    
    for j in range(1,5):
        print(" *", end="")
    print()   
# output:
# ***** 
# *****
# *****
# *****
for i in range(1, 5):
    
    for j in range(i):
        print(" *", end="")
    print()   
# output:


for i in range(5,1,-1):
    
    for j in range(i-1):
        print( " *", end="")
    print()   
# output:    
for i in range(1, 2):
    
    for j in range(1):
        print(" *", end="")
for i in range(1, 2):
    
    for j in range(2):
        print(" *", end="")  
    print()    

for i in range(1, 6):
    
    for j in range(1,1+i):
        print(j, end="")
    print()    
for i in range(6, 1, -1):
    
    for j in range(1,i-1):
        print(j, end="")
    print()  


 
