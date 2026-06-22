n = input("enter the string")
d = {}
for i in n:
    if i in d:
        d[i] +=1
    else:
        d[i]= 1
max = max(d , key =d.get)
print(" Maximum frequency: " , max)   