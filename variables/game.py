'''
password = input("Enter your password: ")
upper = any(i.isupper() for i in password)
lower = any(i.islower() for i in password) 
digit = any(i.isdigit() for i in password) 
special = any(i in "!@#$%^&*()-+" for i in password)
length = len(password) >= 8
upper and lower and digit and special and length == True
print("valid")    
'''
n = "aaabbbcde"
d = {}
count = 0 
for i in n:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
for i in d: 
    if d[i] == 1:
        print(i+str(d[i])) 
          