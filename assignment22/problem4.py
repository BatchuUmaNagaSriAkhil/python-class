class Student:

    def __init__(self, roll_no, name, attendance):
        self.roll_no = roll_no
        self.name = name
        self.attendance = attendance

    def attendance_percentage(self):

        total = len(self.attendance)

        if total == 0:
            return 0

        present = self.attendance.count('P')

        return (present / total) * 100

    def longest_streak(self):

        max_streak = 0
        current = 0

        for ch in self.attendance:

            if ch == 'P':
                current += 1

                if current > max_streak:
                    max_streak = current

            else:
                current = 0

        return max_streak


n = int(input())

students = []

highest = 0
topper = ""

for i in range(n):

    roll_no = input()

    name = input()

    attendance = input()

    s = Student(roll_no, name, attendance)

    students.append(s)

    per = s.attendance_percentage()

    if per > highest:
        highest = per
        topper = s.name


print("Attendance Percentage:")

for s in students:

    print(
        s.name,
        "-",
        round(s.attendance_percentage(), 2),
        "%"
    )


print("Students Below 75%:")

for s in students:

    if s.attendance_percentage() < 75:
        print(s.name)


print("Longest Present Streak:")

for s in students:

    print(
        s.name,
        "-",
        s.longest_streak()
    )


print("Attendance Topper:")
print(topper, "-", round(highest, 2), "%")