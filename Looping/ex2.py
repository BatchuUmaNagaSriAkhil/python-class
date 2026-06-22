#write a program by using  all loop control statements (break, continue, pass) in one program
for i in range(1, 11):
    pass
    if i == 5:
        continue
    if i == 9:
        break
    print(i)   

#summary:
'''
difference between fro and while
for: used whrn num of iterations are known
best for iterating over a sequence 
while:unknown num of iterations
best for condition based loops
best for condition based reputations
It executes untill the condition is true

Q2:What makes the loop infinite?
when condition never meets false beacomes an infinite loop


Q3:can we use else with while loop? A)yes 

i =1
while i<=5:
    print(i)
    i += 1
else:
    print("Loop is finished")
note:else wont work if there is a break statement in the loop

'''