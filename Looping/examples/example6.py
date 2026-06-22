#example6
#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):

    for j in range(n,i-1,-1): #range(start, stop, step) fuction used to print the numbers in decreasing order
        print(j, end=" ")

    print() 
               