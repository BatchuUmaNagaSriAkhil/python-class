'''


Error:An error is a problem in the program causing abnormal termination

1.Syntax Error
2.Run time errors --Exceptions
    ---> Occurs while executing the program

    Example:
    a = 10
    b = 0
    c =a/b --> ZeroDivisionError

    3.Logical Errors:
    Program runs but gives wrong output
    Example:

    print(2*(3+5))

what is exception handling:
Exception handling is a mechanism to handle 
run time errors gracefully without stopping the program

without exception:
1.Program crashes
2.Poor User experience
3.Data loss possible

with exception:
1.Program will execute manually
2.Proper error message
3.Safer application

#basic Exception:
syntax:

keywords:try,catch,finally,raise

try:
   risky code
except:
   handling code


'''

#lets write our first program
#try:
 #   num = int(input("Enter a number:"))
  #  print(10/num)
#except:
 #   print("Some error occured")

#Risky code will be inside try
#if exception occurs ->except executes

#above is not a good practice
#Hides actual problem
#difficult to debug
try:
    num = int(input("Enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide with 0")

except ValueError:
    print("Input should not be a string")


'''
Common python exceptions:
1.ZeroDivisionError ---> Divide with 0
2.ValueError: ---> Invalid input
3.TypeError: ---> Wrong datatype
4.IndexError ---> Invalid Index
5.KeyError ---> Invalid dictionary key
6.FileNotFoundEroor ---> File Missing
7.Attribute Error ---> Invalid Attribute
8.NameError ---> Variable is not defined

'''
#Example:
try:
    list = [10,20,30]
    index = int(input("Enter the index:"))
    print(list[index])

except IndexError:
    print("Index out of range:")

except ValueError:
    print("Please enter integer:")

#Else:if no exception occurs 
'''
try:
   code
except:
   handling
else:
   success block

'''
try:
    list = [10,20,30]
    index = int(input("Enter the index:"))
    print(list[index])

except IndexError:
    print("Index out of range")

except ValueError:
    print("Please enter integer")

else:
     print("No Exception Occured")

#another Example:
try:
    num = int(input("Enter the number:"))
    result = 100/num
except ZeroDivisionError:
    print("Zero")
else:
    print(result)

#finally
'''
finally block executes always
used for:
1.closing files
2.closing database connections
3.cleanup activities

try:
   code
except:
   handling
finally:
   cleaning code
'''
#try:
 #   File = open("data.txt")

#except FileNotFoundError:
#   print("File not found")

#finally:
#    print("Execution completed")
try:
    print("transactiion is processing")
except:
    print("Transaction failed")
finally:
    print("Thanks for using ATM")

try:
    a = 10/0
except ZeroDivisionError as e:
    print("Error:",e)

#Nested try blocks
try:
    print("outer try")
    try:
        num = int(input("Enter number"))
        print(10/num)
    except ZeroDivisionError as e:
        print("Error:",e)
except:
    print("Outer Exception")

#generate exceptions

age = int(input("Enter the age:"))
if age<18:
    raise ValueError("Age should be 18 or greater:")
print("Eligible")

#why custom exceptions:

class MyException(Exception):
    pass
#Bank Application:

class InsufficientBalance(Exception):
    pass

balance = 5000
withdraw = int(input("Enter the amount:"))
if withdraw > balance :
    raise InsufficientBalance("Not enough balance")
print("Withdraw successful")


#Task:write a custom exception
class Chicken(Exception):
    pass
cost = 120
money = int(input("enter the money:"))
if money < cost:
    raise Chicken("Not enough money")
print("Chicken is bought")

#STudent Result System
class Student:
    def __init__(self,marks):
        self.marks = marks
    def calculate_result(self):
        try:
            average = sum(self.marks)/len(self.marks)
            print(average)
        except ZeroDivisionError as error:
            print(error,e)

s1 =Student([])
s1.calculate_result()

#login system:

#Login system:
class LoginSystem:
    def login(self,username,password):
        try:
            if username != "admin":
                raise ValueError("Invalid username")
            if password != "admin123":
                raise ValueError("Invalid Password")
            print("Login Successful")
        except ValueError as e:
            print("Error",e)

'''
Accept account balance and withdrawl amount
raise the exception if 
1.withdrawl amount is negative
2.withdrawl amount exceeds balance
3.withdrawl amount exceeds daily limit of 25000
4.display remaining balance if trasaction successful


'''
class InvalidWithdrawal(Exception):
    pass

balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))

try:
    if withdraw_amount < 0:
        raise InvalidWithdrawal("Withdrawal amount cannot be negative")

    if withdraw_amount > balance:
        raise InvalidWithdrawal("Insufficient balance")

    if withdraw_amount > 25000:
        raise InvalidWithdrawal("Withdrawal amount exceeds daily limit of 25000")

    balance -= withdraw_amount
    print("Transaction Successful")
    print("Remaining Balance:", balance)

except InvalidWithdrawal as e:
    print("Error:", e)