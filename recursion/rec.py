'''
recursion ia a programming technique where a function calls itself
to solve smalleer version & same problem 
function -> calls itself --->again->again

1.Base case:
condition where the recursion stop
2.recursive case:
function calls itself with a smaller one

'''
'''
#def hello(n):
#   print("Hello")
#  #recursive call
# hello(n-1)
#hello(5)
#stack->LIFO(last in frist out)
def fun1():
    print("fun1")
    fun2()
def fun2():
    print("fun2")

fun1()
#added in stack and remove from stack if word
'''
def count(n):
  if n==0:
   return
  print("before:",n)
  count(n-1)
  print("after:",n)
count(5)

'''
def fact(n):
    return n*fact(n-1)
fact(5)

'''
def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)
print(fact(5))
fact(5)
#task:sum of N numbers
def sum(n):
  if n==0:
    return 0
  return n+sum(n-1)
print(sum(5))
#fibonacci:
def fib(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-1)+fib(n-2)
print(fib(5))
#reverse a string
def reverse(a):
  if a=="":
    return ""
  else:
    return a[-1]+reverse(a[:-1])
print(reverse("lokesh"))
'''#take:given with n=1234
#perform the sum of all the digits
#1234 = 1+2+3+4=10'''

def sum_of_digits(n):
  if n==0:
    return 0
  return (n%10) + sum_of_digits(n//10)

print(sum_of_digits(1234))
'''
#check palindrome string using recursion
# I/O="madam"
# O/P=True'''
def palindrome (s = "madam"):
  if len(s)==0:
    return 0
  if s[0] == s[-1] and s[1:-1]:
    return True
  else:
    return False 
print(palindrome())
'''

#print the numbers from N to 1
#N = 5
#5 4 3 2 1'''
def dk(n):
  if n==0:
    return 
  print(n,end="")
  dk(n-1)
dk(5)
'''
#find the largest element in an array using recursion
#I/P:[3,9,2,15,7]
#O/P:15
# Find the largest element in an array using recursion
'''
def find_largest(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_of_rest = find_largest(arr, n - 1)
        return max(arr[n - 1], max_of_rest)


arr = [3, 9, 2, 15, 7]
print(find_largest(arr, len(arr)))

