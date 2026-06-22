names = "tat"
reverse = ""
for i in names:
    reverse= i + reverse
print(reverse)


name = "hello"
reverse = ""
for i in range(len(name)-1,-1,-1):
    reverse += name[i]
print(reverse)