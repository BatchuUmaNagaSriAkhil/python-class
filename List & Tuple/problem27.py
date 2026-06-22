'''
check an array is palindrome using two pointers

'''
n = int(input())

a = list(map(int, input().split()))

left = 0
right = n - 1

is_palindrome = True

while left < right:
    if a[left] != a[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")