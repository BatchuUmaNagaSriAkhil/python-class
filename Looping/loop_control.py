'''
    Loop control:
Break: It stops the execution of the loop immediately and exits the loop.
(Terminates the loop immediately)

continue:skips the current iteration

pass: do's nothing
'''
#Example of break
i = 1
while i<=10:
    if i == 5:
        break
    print(i)
    i += 1
#Example of continue: skips the current iteration and moves forward
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
#Example of pass: do's nothing (provides a placeholder for code)
for i in range(1, 11):
    pass
    