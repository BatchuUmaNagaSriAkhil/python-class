
arr = list(map(int, input("Enter elements: ").split()))
count = 0
a = arr[0]

for i in range(len(arr)):
    if a <= arr[i]:
        count += 1

print(count)
