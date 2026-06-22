#Problem 7: Frequency Leader
n = input()
d = {}
for i in n:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
max = max(d, key =d.get)
print("Maximum frequency : ",max)

#Problem 1: Binary Triangle Pulse
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end="")
    print()

#Problem 2: Cross Matrix Pattern
n = int(input())

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print("-", end="")
    print()

#Problem 3: Wave Number Pyramid   
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(1, i + 1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    print() 

#Problem 4: Alphabet Hourglass   
n = int(input())
k = 65
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(k + j), end="")
    print()

for i in range(n - 2, -1, -1):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(k + j), end="")
    print() 

#Problem 5: Spiral Border Box
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end="")
        else:
            layer = min(i, j, n-1-i, n-1-j)
            print(layer, end="")
    print()   

#Problem 6: Alternate Case Builder
s = input()

for i in range(len(s)):
    if i % 2 == 0:
        print(s[i].upper(), end="")
    else:
        print(s[i].lower(), end="")

#Problem 8: Broken Keyboard Decoder
s = input()

print(s[::2]) 

#Problem 9: Locked Shift Cipher
s = input()
k = int(input())

ans = ""

for ch in s:
    ans += chr((ord(ch) - 97 + k) % 26 + 97)

print(ans)

#Problem 10: Symmetric Split Score
s = input()

left = set()
right = {}

for ch in s:
    right[ch] = right.get(ch, 0) + 1

ans = 0

for ch in s[:-1]:
    left.add(ch)

    right[ch] -= 1
    if right[ch] == 0:
        del right[ch]

    ans = max(ans, len(left & set(right.keys())))

print(ans)