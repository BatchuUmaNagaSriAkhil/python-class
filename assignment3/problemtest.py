'''#A cybersecurity system validates encrypted keywords before granting access.

#A keyword is considered stable if:

#The number of vowels is equal to the number of consonants.
#Numeric characters must not be considered during validation.
#The input string will not contain spaces.
#Write a program to determine whether the given keyword is stable or unstable.

#Input Format
#A single string S
#Output Format
#Print:
Balanced

if the keyword is stable.

Otherwise print:

Not Balanced

Constraints
1 <= length of S <= 200
Sample Input
a1b2e3d

Sample Output
Balanced



Sample Input 1:

a1b2e3d


Sample Output 1:

Balanced
'''
keyword = input("Enter the keyword: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in keyword:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
if vowel_count == consonant_count:
    print("Balanced")
else:
    print("Not Balanced")
    