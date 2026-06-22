
s1 = input("enter the first word: ")
s2 = input("enter the second word: ")

if sorted(s1) == sorted(s2):
    print("Tt is Anagram")
else:
    print("It is Not Anagram")