#Check String Rotation
s1 = input()
s2 = input()

print("Rotation" if s2 in s1 + s1 and len(s1) == len(s2) else "Not Rotation")