'''
Problem 2: Smart Sales Window
Problem Statement
A retail company records daily sales.
Given an array representing sales for N days and a target value K, find the length of the longest 
continuous period whose total sales equal K.
If no such period exists, print -1.
Input
8
3 1 2 4 2 1 1 3
8
Output
4
Explanation
Subarray:
1 2 4 1
has sum 8 and length 4.
Constraints
1 ≤ N ≤ 10^5
-10^4 ≤ arr[i] ≤ 10^4
Skills Tested
 Arrays
 Prefix Sum
 Hashing
 Optimization Thinking
 O(N) Solution Design
'''
class SmartSalesWindow:
    def __init__(self, sales, target):
        self.sales = sales
        self.target = target

    def longest_period(self):
        prefix_sum = 0
        max_length = 0
        prefix_map = {0: -1}

        for i in range(len(self.sales)):
            prefix_sum += self.sales[i]

            if prefix_sum - self.target in prefix_map:
                length = i - prefix_map[prefix_sum - self.target]
                max_length = max(max_length, length)

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_length if max_length > 0 else -1


# Input
n = int(input())
sales = list(map(int, input().split()))
k = int(input())

obj = SmartSalesWindow(sales, k)
print(obj.longest_period())