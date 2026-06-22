'''
Find the common elements in both the lists
'''
a = [1,2,3,4,5,6]
b = [3,4,5,6,7,8]
common = [x for x in a if x in b]
print("common elements:", common)