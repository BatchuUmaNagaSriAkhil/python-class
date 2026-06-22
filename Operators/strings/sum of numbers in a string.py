n = input("enter the string : ")
res = 0
for i in n:
    if "0" <= i <= "9":
        res += int(i)
print(res)  

#Method 2

n = input("enter the string : ")
res = 0
for i in n:
    if i.isdigit():
        res += int(i)
print(res) 