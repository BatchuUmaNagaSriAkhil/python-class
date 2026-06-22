'''
Student Record Management:
write a program to
1.accept student_name and marks
2.store records in a file
named students.txt
3.display all records
4.handle file executions properly

'''
try:
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    with open("students.txt", "a") as file:
        file.write(f"{name} - {marks}\n")

    print("Record saved successfully")

    print("\nStudent Records:")
    with open("students.txt", "r") as file:
        for record in file:
            print(record.strip())

except ValueError:
    print("Marks must be a number")

except PermissionError:
    print("Permission denied")

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)