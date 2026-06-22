n = int(input("Enter the number of rows: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        if i == 0 or i == n - 1 or j == 0 or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()