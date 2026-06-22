#Twin Frequency Strings
from collections import Counter

a = input()
b = input()

if Counter(a) == Counter(b):
    print("YES")
else:
    print("NO")


#Circular Palindrome Rotation    
s = input()

for i in range(len(s)):
    s = s[1:] + s[0]

    if s == s[::-1]:
        print(i + 1)
        break
else:
    print(-1)    