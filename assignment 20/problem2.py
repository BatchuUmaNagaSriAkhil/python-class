#Problem 2 — Online Product Inventory System
class Product:
    def __init__(self, product_name, prices):
        self.__product_name = product_name
        self.__prices = prices

    def get_product_name(self):
        return self.__product_name

    def get_prices(self):
        return self.__prices


class InventoryManager(Product):

    def get_min_price(self):
        return min(self.get_prices())

    def get_max_price(self):
        return max(self.get_prices())

    def count_expensive_prices(self):
        count = 0
        for i in self.get_prices():
            if i >= 1000:
                count += 1
        return count

    def uppercase_name(self):
        return self.get_product_name().upper()

    def is_palindrome(self):
        name = self.get_product_name().lower()
        return name == name[::-1]


product_name = input()
n = int(input())
prices = list(map(int, input().split()))

obj = InventoryManager(product_name, prices)

print("Product:", obj.get_product_name())
print("Uppercase:", obj.uppercase_name())
print("Minimum Price:", obj.get_min_price())
print("Maximum Price:", obj.get_max_price())
print("Expensive Count:", obj.count_expensive_prices())
print("Palindrome:", obj.is_palindrome())