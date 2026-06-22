'''
sliding approach:










'''

arr = [1, 2, 3, 4, 5, 6, 7, 8]

window_size = 4

for i in range(len(arr) - window_size + 1):
    window = arr[i:i + window_size]
    print(window)

arr = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(arr) - 3):
    w1 = arr[i]
    w2 = arr[i + 1]
    w3 = arr[i + 2]
    w4 = arr[i + 3]

    print(w1, w2, w3, w4)


n = int(input())

a = list(map(int, input().split()))

k = 4

for i in range(n - k):
    outgoing = a[i]
    incoming = a[i + k]

    print("Outgoing:", outgoing, "Incoming:", incoming)


n = int(input())

a = list(map(int, input().split()))

k = 4

for i in range(n - k + 1):
    window = a[i:i + k]
    print("Window:", window)

    if i < n - k:
        print("Outgoing:", a[i], "Incoming:", a[i + k])