# Problem 4: ATM Withdrawal Simulator
# Create a mini ATM system. Conditions: PIN must match; Withdrawal amount
# must be multiple of 100; Balance should be sufficient; Minimum balance after
# withdrawal should be ₹1000. Display transaction status.
# Concepts: Variables, Logical expressions, Nested if statements, Arithmetic
# operators
# Sample Input:
# Enter PIN: 1234
# Enter amount: 5000
# Sample Output:
# Transaction Successful
# Remaining Balance = 15000

# Source Code:

# Initial setup
correct_pin = 1234
balance = 20000   # Example starting balance

pin = int(input("Enter PIN: "))

if pin == correct_pin:
    amount = int(input("Enter amount: "))
    
    # Check all 3 withdrawal conditions
    if amount % 100 != 0:
        print("Transaction Failed")
        print("Amount must be multiple of 100")
        print(f"Remaining Balance = {balance}")
    
    elif amount > balance:
        print("Transaction Failed")
        print("Insufficient Balance")
        print(f"Remaining Balance = {balance}")
        
    elif balance - amount < 1000:
        print("Transaction Failed")
        print("Minimum balance ₹1000 must be maintained")
        print(f"Remaining Balance = {balance}")
        
    else:
        balance -= amount
        print("Transaction Successful")
        print(f"Remaining Balance = {balance}")
        
else:
    print("Transaction Failed")
    print("Incorrect PIN")