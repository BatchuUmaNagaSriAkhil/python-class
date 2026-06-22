#Problem 3 — Decorated Attendance
def attendance_check(func):
    def wrapper(name, percentage, medical_leave):
        if percentage >= 75 and medical_leave <= 2:
            return f"{name} Allowed"
        return f"{name} Not Allowed"
    return wrapper


@attendance_check
def student(name, percentage, medical_leave):
    pass


n = int(input())

for i in range(n):
    name, p, m = input().split()
    print(student(name, int(p), int(m)))