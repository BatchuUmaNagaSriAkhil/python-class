#n = input("enter the string")
#s = n.split()
#    res = ""
#    for i in range (len(s)):
#        if i == 0 or i == len(s)-1:
#            res +=s[i].upper()
 #       else:
  #          res +=s[i]    
   # print(res)

n = input("enter the string: ")
s = n.split()
res = []
for i in s:
    if len(i) == 1:
        res.append(i.upper())
    else:
        new_i =(
            i[0].upper()+
            i[1:-1]+i[-1].upper()
        )    
        res.append(new_i)
print("".join(res))        



       
