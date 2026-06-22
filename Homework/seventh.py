# Problem 7: Smart Voting Eligibility System
# A person can vote only if: Age ≥ 18; Has citizenship; Has voter ID. Extra
# condition: Senior citizens (age > 60) get priority voting.
# Concepts: Logical operators, Boolean concepts, Nested if
# Sample Input:
# Age: 65
# Citizen: yes
# Voter ID: yes
# Sample Output:
# Eligible to Vote
# Priority Voting Allowed

# Source Code:

age = int(input("Age: "))
citizen_input = input("Citizen: ").lower()  
voter_id_input = input("Voter ID: ").lower()

if age >= 18 and citizen_input == "yes" and voter_id_input == "yes":
    print("Eligible to Vote")
    if age > 60:
        print("Priority Voting Allowed")
else:
    print("Not Eligible to Vote")   