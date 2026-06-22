#Task: Create a string with your friends names
#name = Manish  Vijay  Ajay
# join the string "_"
# traverse over the string and find the index 
#of the person name starting with "A"
#print the person name
#count the len of the name & check "a" occurances
#print the frnd name with 30 spaces in center

name = "Manish Vijay Ajay" 
names = name.split() 
print(names)
print("_".join(names))
for i in names:
    if i.startswith("A"):
        print(i,"\n",len(i),"\n",i.count("a"),"\n",i.center(30))

