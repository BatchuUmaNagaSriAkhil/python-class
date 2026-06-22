class Order:

    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.amount = amount

    def final_bill(self):
        return self.amount


class VegOrder(Order):

    def final_bill(self):
        return self.amount + (self.amount * 5 / 100)


class NonVegOrder(Order):

    def final_bill(self):
        return self.amount + (self.amount * 12 / 100)


class DessertOrder(Order):

    def final_bill(self):
        return self.amount + (self.amount * 18 / 100)


n = int(input())

orders = []

highest_bill = 0
highest_customer = ""

count_above_500 = 0

for i in range(n):

    order_type, customer_name, amount = input().split()

    amount = float(amount)

    if order_type.lower() == "veg":
        order = VegOrder(customer_name, amount)

    elif order_type.lower() == "nonveg":
        order = NonVegOrder(customer_name, amount)

    elif order_type.lower() == "dessert":
        order = DessertOrder(customer_name, amount)

    orders.append(order)


print("Final Bills:")

for order in orders:

    bill = order.final_bill()

    print(order.customer_name, ":", round(bill, 2))

    if bill > highest_bill:
        highest_bill = bill
        highest_customer = order.customer_name

    if bill > 500:
        count_above_500 += 1


print("Highest Order:")
print(highest_customer, "-", round(highest_bill, 2))

print("Orders Above 500:", count_above_500)