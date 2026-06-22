#Bitwise &
#1 only if both bits are 1
'''
A  B  A&B
1  1  1
0  1  0
0  0  0
1  0  0
'''

#8  4  2  1

#5 ---> 0 1 0 1
#3 ---> 0 0 1 1
#& ---> 0 0 0 1 ---> 1

print(5&3)
print(6&2) #2

'''
Real life:
Permission systems,masking operations
Checking flags
'''
#Bitwise OR
# 1 if any one bit is 1

'''
A B A|B
0 0 0
0 1 1
1 1 1
1 0 1
'''
#Example:
'''
5 ---> 0 1 0 1
3 ---> 0 0 1 1
| --->0 1 1 1 -->7
'''

print(5/3) #7
print(12/4) #12

#Bitwise XOR -->IMP interviews

#1 if boths bits are differents
'''
A B  A^B
0 0  0
0 1  1
1 1  0
1 0  1
'''
'''
6 ---> 0 1 1 0
2 ---> 0 0 1 0
^ ---> 0 1 0 0 -->4

'''
print(6^2) #4

#Swap the numbers without using a 3rd variable
# input = 5, 3
# 0utput = 3, 5

a = 5
b = 3
a = a+b
#a = 5+3 = 8
b = a-b
#b = 8-3 => 5
a = a-b
#a = 8 - 5 => 3

'''
a = a^b
#a = 5^3 -->6
b = b^a
#b = 3^6 -->5
a = a^b
'''
print(a,b)

#Bitwise  Not

# 0 -->1
# 1 -->0

print(~5) #-6

# ~n = -(n+1)

print(~10) #-11

#Low level memory operations

#<< left shift operator

#rule--> shift the bits to left 
'''
5 -->   0 1 0 1
<< -->  1 0 1 0  --->10
'''


print(5<<1)#10

#formula ==> n<<k = n*2^k

#Right shift : shift the bits to right

print(8>>1)

'''
8 --> 1 0 0 0
    0 1 0 0  -->4  
'''

#formula = n>>k = n/2^k
print(16>>2) #4
print(12>>6)

print(13>>7)
print(17>>8)
