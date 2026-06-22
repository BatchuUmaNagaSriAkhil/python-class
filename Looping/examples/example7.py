#example 7
# A
# B C 
# D E F
# G H I J
# K L M N O
n = int(input("Enter the number of rows: "))
k = 65 #ASCII value of A is 65
for i in range(1, n + 1):

    for j in range(i):
        print(chr(k), end=" ") #chr() function is used to convert the ASCII value to character
        k += 1

    print() 