# Problem 1: Secret Mirror Word

s = input("enter the name : ")
reverse = ""
for i in range(len(s)-1,-1,-1):
    reverse += s[i]
print(reverse)






# Problem 2: Vowel Distance Counter

name = "akhil"
count = 0
for i in  name:
    if i.lower() in "a e i o u":
        count += 1
print("vowel count:",count)     


# Problem 3: Circular Shift Match
a = input("enter the name : ")
b = input("enter the name : ")
if len(a) != len(b):
    print("not circular shift")
else:
    circular_shift = False
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            circular_shift = True
            break
    if circular_shift:
        print("circular shift")
    else:
        print("not circular shift")        