'''
check whether a characer is alphabet or not 

'''
#Method-1
n = input("enter the character ")
ascii = ord(n)
if(65 <= ascii <=90) or (97<= ascii <=122):
    print("it is alphabet")
else:
    print("not an alpthabet")    


#Method-2(own)
#s = input("enter the character")
#i = chr(65)
#if  i in range (65,123):
#    s == i
#    print("it is alphabet")
#else:
#    print("not an alphabet")

#find the length of string without
import time
start = time.time()
n = input("enter the string : ")

count = 0
for i in n:
    count +=1
print(count)
print(time.time()-start) 

