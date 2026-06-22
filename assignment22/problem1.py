class Vehicle:
    def __init__(self, vehicle_no, owner_name, hours):
        self.vehicle_no = vehicle_no
        self.owner_name = owner_name
        self.hours = hours

    def calculate_bill(self):
        return 0


class Car(Vehicle):
    def calculate_bill(self):
        return self.hours * 30


class Bike(Vehicle):
    def calculate_bill(self):
        return self.hours * 15


class Truck(Vehicle):
    def calculate_bill(self):
        return self.hours * 50


n = int(input())

vehicles = []

for i in range(n):
    v_type, v_no, owner, hours = input().split()
    hours = int(hours)

    if v_type.lower() == "car":
        vehicles.append(Car(v_no, owner, hours))

    elif v_type.lower() == "bike":
        vehicles.append(Bike(v_no, owner, hours))

    elif v_type.lower() == "truck":
        vehicles.append(Truck(v_no, owner, hours))


total_revenue = 0
max_bill = 0
max_vehicle = None

print("Vehicle Bills:")

for v in vehicles:
    bill = v.calculate_bill()

    print(v.vehicle_no, v.owner_name, bill)

    total_revenue += bill

    if bill > max_bill:
        max_bill = bill
        max_vehicle = v


print("Total Revenue:", total_revenue)

print("Highest Bill Vehicle:")
print(max_vehicle.vehicle_no, max_vehicle.owner_name, max_bill)