#Problem 2 — Generator Password Stream
'''Problem Statement
A password generator yields characters from a string 
S . Generate a password of length 
K by
repeating the string. If the string ends, restart from the beginning. Print the final password.'''
t = int(input())

for i in range(t):
    s = input()
    k = int(input())

    def gen():
        while True:
            for ch in s:
                yield ch

    g = gen()
    password = ""

for i in range(k):
    password += next(g)

print(password)