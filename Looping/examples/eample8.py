#example8
# 1
# 1 3
# 1 3 5
#1 3 5 7 

n = int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j  in range(1, i+1):
        k = 2*j-1
        print(k, end=" ")
    print()  