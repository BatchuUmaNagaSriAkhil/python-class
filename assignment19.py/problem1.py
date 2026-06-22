class SmartLocker:
    def __init__(s,i,o,p):
        s.i,s.o,s.__p,s.__c=i,o,p,0

    def access(s,p):
        if p==s.__p:
            s.__c+=1
            print("Access Granted")
        else:
            print("Invalid PIN")

    def change(s,op,np):
        if op==s.__p:
            s.__p=np
            print("PIN Changed Successfully")
        else:
            print("Incorrect Old PIN")

    def details(s):
        print(f"LockerID: {s.i}")
        print(f"Owner: {s.o}")
        print(f"AccessCount: {s.__c}")

i,o,p=input().split()
l=SmartLocker(i,o,p)

for _ in range(int(input())):
    x=input().split()
    if x[0]=="ACCESS":
        l.access(x[1])
    elif x[0]=="CHANGE":
        l.change(x[1],x[2])
    else:
        l.details()