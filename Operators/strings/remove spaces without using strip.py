#Method 1 using built in function
n = "AKHIL BATCHU"
res = " "
for i in n:
    if i.isalpha():
        res +=i
print(res)
           
#Method 2 without using built in function
n =input("enter the string: ")
res = " "
for i in n:
    if i != " ":
        res +=i
print(res)
                