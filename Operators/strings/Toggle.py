
n =input("enter the string : ")
s = " "
for i in n:
    if i.isupper():
      s +=i.lower()
      
    else: 
        s += i.upper() 
       
print(s)            
