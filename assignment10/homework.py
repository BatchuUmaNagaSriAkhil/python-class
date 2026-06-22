 #Trapping Rain Water (Two Pointers)
n = int(input())
arr = list(map(int, input().split()))
l, r = 0, n - 1
left_max = right_max = 0
water = 0
while l < r:    
    if arr[l] < arr[r]:        
        if arr[l] >= left_max:            
            left_max = arr[l]        
        else:            water += left_max - arr[l]        
        l += 1    
    else:        
        if arr[r] >= right_max:            right_max = arr[r]        
        else:            water += right_max - arr[r]        
        r -= 1
        print(water)
'''Input
63 0 0 2 0 4
Output
10'''

#Problem 2: Merge Two Sorted Arrays (Two Pointers)
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

i = j = 0
res = []

while i < n and j < m:
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

while i < n:
    res.append(a[i])
    i += 1

while j < m:
    res.append(b[j])
    j += 1

print(*res)

#Problem 3: Closest Pair to Target Sum (Two Pointers)
n = int(input())
a = list(map(int, input().split()))
k = int(input())

i, j = 0, n - 1
x, y = a[i], a[j]
d = abs(a[i] + a[j] - k)

while i < j:
    s = a[i] + a[j]

    if abs(s - k) < d:
        d = abs(s - k)
        x, y = a[i], a[j]

    if s < k:
        i += 1
    else:
        j -= 1

print(x, y)
'''
6
1 3 4 7 10 12
15

Output

3 12
'''