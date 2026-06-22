#Problem 1 — Student Result Analyzer System
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks


class ResultAnalyzer(Student):

    def get_average(self):
        marks = self.get_marks()
        return sum(marks) / len(marks)

    def get_highest(self):
        return max(self.get_marks())

    def count_passed_subjects(self):
        count = 0
        for i in self.get_marks():
            if i >= 50:
                count += 1
        return count

    def reverse_name(self):
        return self.get_name()[::-1]


name = input()
n = int(input())
marks = list(map(int, input().split()))

obj = ResultAnalyzer(name, marks)

print("Name:", obj.get_name())
print("Reversed Name:", obj.reverse_name())
print("Average:", obj.get_average())
print("Highest:", obj.get_highest())
print("Passed Subjects:", obj.count_passed_subjects())