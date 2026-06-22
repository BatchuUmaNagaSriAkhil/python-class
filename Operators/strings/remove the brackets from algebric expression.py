n = input("enter the input: ")
res = ""
for i in n:
    if i not in "[]  {}  ()":
        res  += i
print(res)        