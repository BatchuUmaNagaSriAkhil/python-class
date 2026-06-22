#Remove Duplicate Characters
s = input()

print("".join(dict.fromkeys(s)))