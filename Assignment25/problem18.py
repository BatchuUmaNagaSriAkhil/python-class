#Palindrome Numbers in Range
a = int(input())
b = int(input())

result = [str(i) for i in range(a, b + 1) if str(i) == str(i)[::-1]]

print(" ".join(result) if result else "No Palindromes")