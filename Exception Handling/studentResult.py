'''
A university wants to automate student result processing
The program should accept:
1.marks of 5 subjects
2.raise exception
if 
1.marks are negative
2.marks exceed 100
3.non-numeric input
4.calculate average and grade
rules:
avg >=75 ->distinction
avg >=60 ->first class
avg >=40 ->pass

'''
class InvalidMarksError(Exception):
    pass

class StudentResult:
    def __init__(self):
        self.marks = []

    def input_marks(self):
        try:
            for i in range(5):
                mark = int(input(f"Enter the subject{i+1} marks:"))

                if mark < 0 or mark > 100:
                    raise InvalidMarksError("Marks should be btw 0 and 100")
            
                self.marks.append(mark)
            average = sum(self.marks)/5
            print("Average:",average)
            if average >= 75:
                print("Distinction")
            elif average >= 60:
                print("Firstclass")
            elif average >= 40:
                print("Pass")
            else:
                print("Fail")

        except ValueError:
            print("Only numerics are allowed")
        except InvalidMarksError as e:
            print(e)
s1 = StudentResult()
s1.input_marks()
