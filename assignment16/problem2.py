#Problem 2 — Recursive Binary Conversion
n = int(input())

def binary(n):
    if n < 2:
        print(n, end="")
        return
    binary(n // 2)
    print(n % 2, end="")
    

binary(n)
