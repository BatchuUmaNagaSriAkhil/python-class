#Armstrong Number Check
n = int(input())

p = len(str(n))

s = sum(int(digit) ** p for digit in str(n))

print("Armstrong" if s == n else "Not Armstrong")