#Problem 1: Alternate Index Sum
n = int(input())
arr = list(map(int, input().split()))

even_sum = 0
odd_sum = 0
for i in range(n):    
    if i % 2 == 0:        
        even_sum += arr[i]    
    else:        
        odd_sum += arr[i]
print(even_sum, odd_sum)

#Problem 2: Tuple Boundary Product
n = int(input())
t = tuple(map(int, input().split()))
print(t[0] * t[-1])

#Problem 3: Count Smaller Than Key
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0
for i in arr:    
    if i < k:        count += 1
print(count)