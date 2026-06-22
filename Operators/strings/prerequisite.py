'''
count the  frequency of the characters
Example:

input:aabbc
output:
a:3
b:1
c:1

'''
n = input("enter the string: ")
d ={}
for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(d[i])        
    #print(i + ":" + str(d[i])) for printing the all with characters
    