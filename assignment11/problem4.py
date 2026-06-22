problem:4
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # Make the array circular
    circular_arr = arr + arr[:k-1]

    # First window
    window_sum = sum(circular_arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(1, n):
        window_sum = window_sum - circular_arr[i - 1] + circular_arr[i + k - 1]
        max_sum = max(max_sum, window_sum)

    print(max_sum)
    '''
I/P:
1
5 3
8 1 2 4 5
O/P:17'''