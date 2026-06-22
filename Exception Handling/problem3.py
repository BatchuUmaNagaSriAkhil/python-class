'''
a company wants to create a file analyzer tools
a program should accept:
1.Accept fine name from us
handle:
1.file not found
2.permission denied
3.empty file
display:
number of lines
number of words
number o characters

'''
class EmptyFileError(Exception):
    pass

try:
    filename = input("Enter file name: ")

    file = open(filename, "r")
    data = file.read()

    if len(data.strip()) == 0:
        raise EmptyFileError("File is empty")

    lines = len(data.splitlines())
    words = len(data.split())
    characters = len(data)

    print("Number of lines:", lines)
    print("Number of words:", words)
    print("Number of characters:", characters)

    file.close()

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

except EmptyFileError:
    print("Empty file")  