#example 5.a
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):

    for j in range(i):
        print(i, end=" ")

    print()



#example 5.b
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# #1    
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):

    for j in range(1, i + 1):
        print(i, end=" ")

    print()    
            