'''
Find the multiple range queries
1-4
2-5
0-3
all queries in a single program


'''
'''
arr = [2,4,1,7,3]
a = 1
b = 2
c = 3
d = 4
e = 5
f = 0
prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1,d+1):
    prefix[i] =prefix[i-1]+ arr[i]
print(prefix)
sum = prefix[d]-prefix[a-1]
print(sum)
for j in range(b,e+1):
      prefix[i] =prefix[j-1]+ arr[i]
sum1= prefix[e-1]-prefix[b]
print(sum1)
for k in range(f,c+1):
       prefix[i] =prefix[k-1]+ arr[i]
sum2= prefix[c]-prefix[f-0]
print(sum2)
'''

arr = [2, 4, 1, 7, 3, 9]

queries = [(1, 4), (2, 5), (0, 3)]

# Prefix sum
prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("Prefix:", prefix)

# Answer queries
for L, R in queries:
    if L == 0:
        total = prefix[R]
    else:
        total = prefix[R] - prefix[L - 1]

    print(total)