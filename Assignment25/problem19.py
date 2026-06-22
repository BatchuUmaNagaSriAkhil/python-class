#Perfect Number Check
n = int(input())

s = sum(i for i in range(1, n) if n % i == 0)

print("Perfect" if s == n else "Not Perfect")