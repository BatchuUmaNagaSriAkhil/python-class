'''
Create:
Vehicle class with method start()
car class inheriting Vehicle
sportscar class inheriting the car
add method:
speed()
inside the sports car;
call:
start()
speed() using sports car

'''
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car (Vehicle):
    pass
class Sportscar(Car):
    def speed(self):
        print("speed is 200kmph")
sp = Sportscar()
sp.start()
sp.speed()
