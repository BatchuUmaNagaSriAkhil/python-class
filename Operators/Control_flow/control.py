#decision making
#1.how many times to execute and what to execute
#human analogy:
from __future__ import with_statement

'''
if it rains --> take umberella
if marks > 40 --> pass
if password is correct --> login

'''

#program also needs decision making ability
#control flow: determines
#which statement to execute and in what order

'''
3-Types of control flow
1.Sequential :Top to bottom execution
2.conditional: decision making
3.Looping: repetition

'''
#if --> to check the condition
#& executes if condition is true
#Syntax:
# if condition:
#     statements

#Example:
age =21
if age > 20:
    print("Eligible")
    
'''
Execution flow
        condition true?
                |
        Execute the block
        
'''

x = 10

if x>5:
    print("Hello")
    
#if-else  :what if state becomes false

#if condition:
#   statement
#else:
#   statements

# Example:     Even/odd

#take input
num = int(input("Enter a number"))

#check the condition
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
'''
Execution flow
                        condition ?
                        /       \
                    True        False
                        |          |
                        Even      Odd
                        
    '''
    
    # elif ladder
    #Multiple conditions: multiple decisions
    
    #if condition:
    #   statement
    #elif condition:
    #statement
    #else:
    # statement
