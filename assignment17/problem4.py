#Problem 4 — OOP Library Fine System ,Problem Statement :Calculate the total fine for delayed days
class LibraryFine:
    def __init__(self, days):
        self.days = days

    def calculate_fine(self):
        d = self.days

        if d <= 5:
            return d * 2
        elif d <= 10:
            return 5 * 2 + (d - 5) * 5
        else:
            return 5 * 2 + 5 * 5 + (d - 10) * 10


t = int(input())

for _ in range(t):
    d = int(input())
    obj = LibraryFine(d)
    print(obj.calculate_fine())