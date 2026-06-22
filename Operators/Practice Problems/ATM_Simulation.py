'''
Problem Statement:

Simulate the ATM system:
1.Correct pin is required
2.withdraw only if sufficient balance is available
3.intial balance is 20000

'''
pin = int(input("Enter PIN: "))
if pin == 1916:
    amount = int(input("Enter amount: "))
    if amount > 20000:
        print("Transaction Failed")
        print("Insufficient Balance")
        print("Remaining Balance = 20000")
    else:
        balance = 20000 - amount
        print("Transaction Successful")
        print(f"Remaining Balance = {balance}")