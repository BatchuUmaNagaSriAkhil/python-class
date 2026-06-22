#Problem Statement
#A digital display system prints a staircase pattern using binary digits (0 and 1).
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()