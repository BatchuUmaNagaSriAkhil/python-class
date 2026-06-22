#Move Zeros to End
n = int(input())
arr = list(map(int, input().split()))

non_zero = [x for x in arr if x != 0]
zeros = [0] * arr.count(0)

print(*(non_zero + zeros))