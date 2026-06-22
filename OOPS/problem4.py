'''
E_Commerce Shopping Cart
Create a class ShoppingCart
Features:
1.private var - __total
2.add items
3.remove the items
4.apply discount

Rules:
1.Total should never become zero
2.Discount only if total > 1000

Methods:
1.add_item(price)
2.remove_item(price)
3.apply_discount(percent)
4.get_total()

'''
class ShoppingCart:
    def __init__(self, total):
        if total <= 0:
            print("Total should never be zero")
            self.__total = 1
        else:
            self.__total = total

    def add_item(self, price):
        self.__total += price
        print(f"Item added: {price}")

    def remove_item(self, price):
        if self.__total - price <= 0:
            print("Total should never become zero")
        else:
            self.__total -= price
            print(f"Item removed: {price}")

    def apply_discount(self, percent):
        if self.__total > 1000:
            discount = self.__total * percent / 100
            self.__total -= discount
            print(f"Discount applied: {percent}%")
        else:
            print("Discount applicable only if total > 1000")

    def get_total(self):
        return self.__total

cart = ShoppingCart(1200)

cart.add_item(300)
cart.remove_item(200)
cart.apply_discount(10)

print(cart.get_total())