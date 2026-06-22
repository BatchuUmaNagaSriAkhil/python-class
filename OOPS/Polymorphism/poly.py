'''

What is polymorphism?
poly --> Many
morphism -> forms
same method/operators will behave differently

Example:

print(5+3) #8
print("Hello"+"world")#Helloworld

            same operator
                |
            But diff behaviours

Types of polymorphism
1.compile time
2.run time polymorphism
'''

#1.compile time --> method overloaing
'''
no method overloading in python

method overloading:
it is method name + different parameters
it is not possible in python
to overcome or to handle overloadingin python , python uses *args(variable length arguments)

method overloading:
is same method names + same parameters
is possible in python

#java --> add(int,int)
#  ---> add (int,int,int)

python approach:
class calculator:
    def add(self,a,b,c = 0):
        print(a + b + c)

c1 = calculator()
c1.add(10,20)
c1.add(10,20,30)
'''
#2.Run time polymorphism
'''
-->using method overriding
'''
class Bird:
    def fly(self):
        print("Bird")
class Eagle(Bird):
    def fly(self):
        print("Eagle's flying")
c = Eagle()
c.fly()

#Duck typing in python
#python focuses on behaviour not object type
class Duck:
    def sound(self):
        print("Quack")
class Dog:
    def sound(self):
        print("Bark")
def make_sound(obj):
    obj.sound()
d1 = Duck()
d2 = Dog()

make_sound(d1)
make_sound(d2)
