class Employee:

    def __init__(self, emp_id, name, skills):
        self.__emp_id = emp_id
        self.__name = name

        # remove duplicate skills
        self.__skills = list(set(skills))

    def get_name(self):
        return self.__name

    def get_skills(self):
        return self.__skills

    def skill_count(self):
        return len(self.__skills)


n = int(input())

employees = []

all_skills = set()

max_emp = None
max_count = 0

print("Enter employee details:")

for i in range(n):

    emp_id = input()
    name = input()

    skills = input().split(",")

    emp = Employee(emp_id, name, skills)

    employees.append(emp)

    # store all unique skills
    for skill in emp.get_skills():
        all_skills.add(skill.strip().lower())

    # employee with maximum skills
    if emp.skill_count() > max_count:
        max_count = emp.skill_count()
        max_emp = emp


print("Unique Skills Count:", len(all_skills))

print("Employee with Maximum Skills:")
print(max_emp.get_name(), "-", max_count)

print("Employees knowing Python:")

for emp in employees:

    skills = [s.lower().strip() for s in emp.get_skills()]

    if "python" in skills:
        print(emp.get_name())