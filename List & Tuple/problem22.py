'''
find the frequency of the element
i/p:[1,2,2,3,3,3]
o//p:[1,2,3]

'''
n = int(input())

a = list(map(int, input().split()))

freq = {}

for num in a:
    freq[num] = freq.get(num, 0) + 1

for key in freq:
    print(key, "->", freq[key])