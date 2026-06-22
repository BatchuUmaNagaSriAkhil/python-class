'''

a mechanism where one class aquirence of another class
                        OR
one class reuses the features of another class

Simple Understanding:
a class can 

use variables
use methods of parent class

Example:
vehicles:
car,bike,bus

All vehicles have
start(),stop()
No need to repeated code

write code once
|
use num of times

Advantages or why?
1.Code Reusability
2.Reducing the code duplication
3.Better Organization
4.Easy Maintenance

Terms:
Parent: Base or Supoer Class
Child: Sub Class/Derived

            Parent
                |
            Child

'''
#syntax:
class Parent:
    pass

class Child(Parent):
    pass

#Basic Example:
class Animal:
    def eat(self):
        print("Animal is eating")
        
#child class
class Dog(Animal):
    pass

#having to create object
# for child class
d1 = Dog()
d1.eat()
'''
Dog class does not contains eat()
                |
    python searchs in animal class
                |
    Method is found and executed

'''
#No Inheritance

class Dog:
    def eat(self):
        print("eating")

class Cat:
    def eat(self):
        print("eating")

#with inheritance
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass
class Cat(Animal):
    pass
c1 = Cat()
c1.eat()

 
#accessing the parent variable
class Person:
    def __init__(self):
        self.name = "Glory"
class Student(Person):
    pass

s1 = Student()
print(s1.name)

'''
Types of inheritance in python
1.Single Inheritance
2.Multiple Inheritance
3.Multilevel Inheritance
4.Hierarichal Inheritance
5.Hybrid Inheritance


1.Single Inheritance:
One child class inherits one parent class

                Parent
                   |
                Child

'''
#example:
class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("Barking")

d1 = Dog()
d1.eat()
d1.bark()

'''
2.Multiple Inheritance:

One child class inherits
from multiple parents

            Parent1       Parent2
                \            /
                    Child
                
'''
#example
class Father:
    def money(self):
        print("Father's Money")

class Mother:
    def gold(self):
        print("Mother's Gold")

class Child(Father,Mother):
    pass
c1 = Child()
c1.gold()
c1.money()

'''
3.Multilevel Inheritance:
Inheritance chain of multiple levels

            Grand Parent
                 |
               Parent
                 |
               Child
'''
class Grandparent:
    def house(self):
        print("Grand Parents Home")

class Parent(Grandparent):
    def car(self):
        print("Parents car")

class Child(Parent):
    def bike(self):
        print("Child's Bike")

c1 = Child()
c1.house()
c1.car()
c1.bike()

'''
4.Hierarichal Inheritance:

Multiple child classes inherits from single or one parent

                        Parent
                         /   \
                    Child1   Child2
'''
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")
class Cat(Animal):
    def meow(self):
        print("Meow")

c1 = Cat()
c1.eat()
'''
5.Hybrid Inheritance:
two or more inheritance types:
1.hierarichal and multiple

                    A
                   /  \
                   B   C
                   \   /
                     D

'''
class A:
    def show_a(self):
        print("Class A")
class B:
    def show_b(self):
        print("Class B")
class C(A):
    def show_c(self):
        print("Class C")

class D(B,C):
    def show_d(self):
        print("Class D")

d1 = D()
d1.show_a()
d1.show_b()
d1.show_c()
d1.show_d()

#check the inheritance
class Amnimal:
    pass
class Dog(Animal):
    pass
c1 = Dog()

print(isinstance(c1,Dog))
print(issubclass(Dog,Animal))

class parent:
    def __init__(self):
        print("Constructor called")
class Child(parent):
    pass

c1 = Child()
