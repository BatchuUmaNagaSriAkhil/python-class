'''
Anology:
you are given with 2 programs where it is generated

how will you decide which one to use?
1.faster program
2.less memeory
3.efficient

algorithm complexity == efficienty

two types
1.time complexity: fast results in google

2.space complexity      
                                    Mark-zukerberg -->CSS 20KB
                                     /            \
                                    A = 19kb     B = 18kb
                                     10LPA         30LPA

Time complexity:
Time complexity measures how the running time grows as the size of input

3 -Techniques to measure time complexity

'''
#stop watch method:
import time
start = time.time()
for i in range (1,1001):
    print(i)
print(time.time()-start)    

'''
problems in abou technique
1.different systems diff time
2.Different compilers/diff interpreters
3.background apps effect time
4.Internet/CPU/GPU/ affect the perfomance
'''
#technique - 2 Counting the num of operations
#Not measures the time in seconds but counts operations
def c_to_f(c):
    return c*9/5+32 #3 operations
#Example 2 
def mysum(x):
    total = 0 #1 operation
    for i in range(x+1):
        total = total+i  #2 operation
    return total     #1+2x operations

#Technique-3 Order of growth
'''
Notations:
asymptotic notation

1.Big Oh o():calc the upper bound(worst time complextiy)
2.Omega Notation : Best case complexity
3.theta : avg case complexity

#example : Linear search
arr = [1,2,3,4,5,6,7]

arr[0] == target # best case 
arr[3] == target #avg case
arr[last] == target #worst case

Big Oh: worst time growth
focus:
1.Measuring the scalability
2.machine independent
3.focuses on growth
4.Ignores the hardware

def mysum(n):
    total = 0 #1 operation
    for i in range(n+1):
        total = total+i  #2 operation
    return total    
     #1+2n operations

Big Oh (rules)
1.additive constants(remove)
#1+2n ---->2n
2.multiplicative constant(remove)
#2n ---> n 
        time complexity --->O(n)     

a = 10
b = 20
c = a+b

for i in range (1,101):
O(n)

#nested loops
fro i in range(1,n+1):
    for j in range(i):
        print(i)

Equation: n^2+n+10 --->n^2+n --> O(n^2)

for i in range(1,100)
    print(i)
for j in range(1,50)
    print(j)

    n+n --> 2n -->O(n)
#practice:
1.n^2+1000n+3^1000

O(n^2)

2.log(n)+n+4
O(n)
3.0.00001*n*log(n)+300n
O(nlog(n))
4.2n^30 + 3^n
O(3^n)

#Complexity classes

1.Constant time -->O(1) 
_> same time always
arr =[10,20,20]
arr[i]       
-->Input increases and time stays constant

2.Linear time -->O(n)
for i in arr:
print(i)
#Grows along with input

#.Quadratic time -->O(n^2)

#nested loops
fro i in range(1,n+1):
    for j in range(i):
        print(i)

#Outer loop runs n times and 
inner loop runs n time with outerloops

4.Logarithmic Time --> O(log(n))

Best Example:

Binary Search:
arr = [1,6,8,3,7,10]
arr =[1,3,6,7,8,10]

n/2 

#large input :smaller growth
#Very efficient

5.Lineararthimic -->O(n log(n))

#Better than quadratic
#used in industry

6.exponential: -->O(2^n)

very slow ,not much used
Example: recursive fibonacii
Dangerous for large input
while n>1:
n = n // 2
#loop diving 2 -->O(log(n))

#Space complexity: Measures memory used by the algorithm
1.Input space
2.Auxiliary space
Example:
a = 10
b = 20

constant space ---> O(1)

Example-2:
arr = [0]*n
linear space --->O(n)







'''
