'''
find the maximum in a tuple
'''
n =(10,20,30,40,50)
max = n[0]
for i in n:
    if i > max :
        max = i
print(max)