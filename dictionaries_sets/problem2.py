'''
Create a dict with employee details
now add branch and phone number at a time 
fetch all the key and values using loop
make sure to copy before deleting any pair
pop the last added pair
print the pairs without deleting


'''
employee = {
    "e1": {
        "Name": "Anas",
        "salary": 25000
    },
    "e2": {
        "Name": "Akhil",
        "salary": 45000
    },
    "e3": {
        "Name": "Lokesh",
        "salary": 30000
    }
}

employee["branch"] = "Hyd"
employee["phone"] = "9"

print("After adding branch and phone:")
print(employee)

print("\nKeys and Values:")
for key, value in employee.items():
    print(key, ":", value)

employee_copy = employee.copy()

last_pair = employee.popitem()
print("\nPopped last added pair:")
print(last_pair)

print("\nCopied dictionary:")
for key, value in employee_copy.items():
    print(key, ":", value)