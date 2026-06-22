'''
Employee skill system
create;
class Programmer with method coding()
class Designer with method designing()

create a child class Employee inheriting
both classes
call both methods using Employee objects

'''
class Programmer:
    def coding(self):
        print("Coding")
class designer:
    def designing(self):
        print("Designing")
class software_developer(Programmer,designer):
    pass
e1 = software_developer()
e1.coding()
e1.designing()
