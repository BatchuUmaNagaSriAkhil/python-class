'''
what is dict?
list --> collection of ordered elements
mutable --> can be modified
tuple -->collection of ordered elements
Immutable  --> cant be modified

dict: collection of key value pairs

      key: values
      91:"Anas"
      dict : {}
   
#Mutable:can be modified
#'keys' are immutable and values are immutable
Not allows duplicates of-- keys
values  can be duplicates
No fixed indexing
searching is very efficient: O(1)
dict uses hashing technique to search hence O(1)

why we use dict?
1.Labels
2.Properties
3.Mapping the relationships


list = ["Anas","91",21]

#creation of dictionary
student = { 
    "Name":"Anas",
    "RollNo":91,
    "Age":21

}
print(student)
'''
#creation of dictionary
Student = { 
    "Name":"Anas",
    "RollNo":91,
    "Age":21

}
print(Student)


#2nd method
student = dict(name = "Venu",
               age = 21,Branch = "CSE-DS")

print(student)

#3rd Method: empty dict

data = {}

print(data)

#list =[10,20,30,40]
#       # 0 1 2 3
# list[0]

print(student["name"])
print(student["age"])
'''

feature         List    dict
ordered          yes      no
access(indexing) yes     keys no
arr[0]           yes      student[keys]

'''

employee = {}

employee["Name"] = "Kowshik"
employee["age"] = "21" 

print(employee)


#update the age
employee["age"] = "23" 
print(employee)

#delete the value
employee.pop("age")
print(employee)

#2nd method of delete

del Student["RollNo"]
print(Student)

#dictionary methods
print(student.keys())

#values() -->return all the values
print(student.values())

#items() -->return all the items in dict
print(student.items())

#print(student["Branch"])
#when I use this --> keyerror


#access the elements
print(Student.get("Branch"))
#None


#update() --> add multiple elements
Student.update({"Branch":"CSE","College":"CITY"})

print(Student)

#popitem: removes the last inserted pair
Student.popitem()
print(Student)


#looping on dictionary
for i in student:
    print(i)

#iterating on values
for value in student.values():
    print(value)

for key,value in student.items():
    print(key,value)


#Nested dictionaries: dict indside dict
students = {
    "s1":{
        "Name":"Rajesh",
        "Branch":"AI"
    },
    "s2":{
        "Name":"Ravi",
        "Branch":"AIML"
    }
}
print(students["s1"]["Name"])

#can i store list inside the dict?
student ={
    "Name":"Harish",
    "Marks":[90,80,60,95]
}

print(student)

#we can store multiple dict in list

students =[
    {"Name":"Rajesh","Branch":"CSE"},
        #0
    {"Name":"Praful","Branch":"CSD"}
        #1
]

students[0]["Name"]
print(students)

#Dict comprehension

#{key:value for variable in iterable}

squares = {X:X*X for X in range(1,11)}
print(squares)

#keys: Rules
'''
integers
strings
tuple
list --- no
dictionary --> 

student ={
    1:"Anas",
    "Roll":91,
    (1,2):"tuple"
    [1,2,3]:"List" #Mutable
    {"Name":"Manish}:"Hello" #can't use    
}


'''