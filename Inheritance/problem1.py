'''

Problem:1
create a parent class Animal with method sound() that should print animal makes sound


'''
class Animal:
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    pass
c1 = Dog()
c1.sound()