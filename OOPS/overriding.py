'''
Method Overriding?
Redefining a parent class method

inside the child class

-same method name
-same parameters

child class method changes the
behaviour of parent classmethod

speak()
'''
class Animal:
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    #same name as parent class
    def sound(self):
        print("Dog Barks")
d1 = Dog()
d1.sound()

'''
Dog object calls sound 
|
Python will searches inside
|
Method found
|
Parent ignored

Animal
    sound()
     |overridden by
    Dog
      sound()

#Important rule:Method name should be same as in child name

'''
'''
Super():super function

Accessing Parent class methods
'''
class Parent:
    def show(self):
        print("Parent Method")
class Child(Parent):
    def show(self):
        #call the parent method
        super().show()
        print("Child Method")
class GrandChild(Child):
    def show(self):
        #call the parent method
        super().show()
        print("GrandChild Method")

c1 = GrandChild()
c1.show()

#Is it possible to over constructor
class Parent:
    def __init__(self,name):
        self.name = name
        print("Parent constructor")

class Child(Parent):
    def __init__(self,name):
        super().__init__(name)
        print(self.name)
        print("Child Constructor")

c1 = Child("Anas")
print(c1.name)
'''
MRO:Method Resolution Order
order in which python searches methods
'''
class A:
    def show(self):
        print("class A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

d1 = D()
d1.show()

#prints order
print(D.mro())