
'''
Problem 1: Employee Productivity Analyzer
Topics Covered: Strings, Dictionaries, Lists, Functions, Sorting, OOPs
Problem Statement
A company tracks employee activities using the format:
Employee Name: TaskCompleted
The activities are stored in a list.
You need to generate a productivity report.
Rules
1. Count the number of tasks completed by each employee. 
2. Employee names are case-insensitive. 
3. Print employees in descending order of tasks completed. 
4. If two employees have the same task count, print them in alphabetical order. 
Input
7
John:Login
Alice:Testing
john:Development
Alice:Documentation
Bob:Testing
John:CodeReview
alice:BugFix
Output
john 3
alice 3
bob 1
Constraints
1 ≤ N ≤ 10^4
Skills Tested
 String Parsing
 Dictionaries / Hashing
 Frequency Counting
 Sorting with Custom Logic
 Functions


'''

class ProductivityAnalyzer:
    def __init__(self):
        self.employee_tasks = {}

    def add_activity(self, activity):
        name, task = activity.split(":")
        name = name.lower()  # case-insensitive

        if name in self.employee_tasks:
            self.employee_tasks[name] += 1
        else:
            self.employee_tasks[name] = 1

    def generate_report(self):
        result = sorted(
            self.employee_tasks.items(),
            key=lambda x: (-x[1], x[0])
        )

        for name, count in result:
            print(name, count)
c

# Input
n = int(input())

analyzer = ProductivityAnalyzer()

for _ in range(n):
    activity = input()
    analyzer.add_activity(activity)

analyzer.generate_report()