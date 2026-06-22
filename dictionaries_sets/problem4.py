'''
Top k frequent elements
input:[1,1,1,2,2,3]
k = 2
output: [1,2]


'''
a = [1,1,1,2,2,3]
k = 2
d = {}
for i in a:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
result = sorted(d,key=d.get,reverse =True)
print(result[:k])