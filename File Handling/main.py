'''
Files helps store data permanently

File: Collection of information OR Data

File Handling:
it is a process of
1.Creating files
2.Reading the files
3.Writing files
4.Updating files
using Python

why file handling?
Data disappears after the program ends

With files:
1.Store data perm
2.Data sharing possible
3.Reports/logs can be generated

Types of files ???
1.Text Files:
1. .txt
2. .csv
3. .py
4. .json

2.Binary Files:
1.Images
2.Videos
3.Pdf's

Opening the files
#syntax:

file =open("Filename","mode")

print(file)

'''

'''
File Models
Mode      Meaning
r         read
w         write
a         append
x         create
r+        read+write
w+        write+read
a+        append+read
rb        read binary
wb        write binary

'''
try:
    file = open(r"C:/Users/Happy/Desktop/summer training/File Handling/data.txt","r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError as e:
    print("No File Found")


#write mode - w
file = open(r"C:/Users/Happy/Desktop/summer training/File Handling/data.txt","w")
file.write("Hello Students")
file.close()

#Creates files if not exist
#deletes the old and add new content




#append - mode: adds the data at the end
file = open(r"C:/Users/Happy/Desktop/summer training/File Handling/data.txt","a")
file.write("\nHow are you")
file.close()

#create mode:x
#file = open("newfile.txt","x")

#Gives FileExistsError if already exists

#Read()
file = open("newfile.txt","r")
print(file.read())
file.close()

#readline()
file = open("newfile.txt","r")
print(file.readline())
file.close()
#3.readlines()-reads multiple lines
file = open("newfile.txt","r")
lines = file.readlines()
print(lines)
file.close()

#write() --> writes the data to file
file = open("newfile.txt","w")
file.write("Anas\n")
file.write("Akhil\n")
file.close()

#writelines(): writes list data
names = [
    "Varfan\n",
    "Lokesh\n",
    "Anas"

]
file = open("newfiles.txt","w")
file.writelines(names)
file.close()

#Pointer methods:
# returns the current cursor position
#tell()
file = open("newfiles.txt","r")
print(file.tell())
file.read(5)
print(file.tell())
file.close()

#seek(): Moves the cursor position
file = open("newfiles.txt","r")
file.seek(3)
print(file.read())
file.close()

#with open()

with open("newfiles.txt","r") as file:
    print(file.read())

#automatic closing

name = input("Enter student name:")
marks = input("Enter marks:")
with open("newfile.txt","a") as file:
    file.write(name + ""+ marks + "\n")
print("Record Saved")

#list --employee details
employees = [
    "Imran 50000",
    "Venu 60000",
    "Kowshik 100000"
]
with open("newfile.txt","w") as file:
    for emp in employees:
        file.write(emp + "\n")
print("Report Generated")

'''
CSV--> Comma Seperated Values
used:excel,reports,databases

Example:
name,age,branch
akhil,21,ds
lokesh,20,ds
Anas,20,ds


 '''
import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Rahul","23","CSE"])
    writer.writerow(["Lokesh","21","DS"])
    writer.writerow(["Akhil","21","DS"])
    writer.writerow(["Anas","21","DS"])


#Read CSV
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Binary file handling
file = open("dark.jpeg","rb")
data = file.read()
print(data)
file.close( )

#Task1:count words in a file:

with open("newfile.txt","r") as file:
        content = file.read()
        words = len(content.split())
        print(words)

#Task2:Count lines in a file
with open("newfile.txt","r") as file:
    lines = len(file.readlines())
    print(lines)

# Task 3: Search a word in a file

word = input("Enter the word: ")

with open("newfile.txt", "r") as file:
    content = file.read()

    if word in content:
        print("Word Found")
    else:
        print("No Word")

#Task4:Copy one file to another
# Copy content from one file to another

with open("newfile.txt", "r") as source:
    content = source.read()

with open("newfiles.txt", "w") as destination:
    destination.write(content)

print("File copied successfully")

#Task5:Count Characters in a file
with open("newfile.txt", "r") as file:
    content = file.read()

print("Number of characters:", len(content))
with open("newfiles.txt","r") as file:
    content = file.read()
print("Number of characters", len(content))

