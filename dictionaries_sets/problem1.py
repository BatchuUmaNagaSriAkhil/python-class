'''
text ="apple banana pineapple strawberry banana apple"
find the frequency of the words?

'''
text = ("apple banana pineapple strawberry banana apple")
d = {}
for i in text.split():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

'''
#shalloo copy:

'''
student = {
    "name":"Anas",
    "RollNo":91
}
b = student.copy()
print(b)

student["RollNo"] = 9
print(student)

print(b)

c = student
print(c)

student["RollNo"] = 10
print(c)


#why dict is faster

#Hashing -- dict stores data in hashtable
#Time complexity: O(1)
# searching --> O(1)
#insert,deletr --> O(1)

data = {
    "a":1,
    "a":2
}
print(data)