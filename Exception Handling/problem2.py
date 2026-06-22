'''
An E-commerence company wants to vallidate order processing
the system should accept:
1.product stock
2.payment status
3.delivery address
raise exception if:
1.stock un available
2.payment fail
3.address is empyt
if al validation pass:
print("order successfully placed")

'''
class Unavailable(Exception):
    pass

class Fail(Exception):
    pass

class Empty(Exception):
    pass


class Ecommerce:
    def __init__(self):
        self.stock = int(input("Enter product stock: "))
        self.payment_status = input("Enter payment status (success/fail): ")
        self.address = input("Enter delivery address: ")

    def place_order(self):
        try:
            if self.stock <= 0:
                raise Unavailable("Stock unavailable")

            if self.payment_status.lower() != "success":
                raise Fail("Payment failed")

            if self.address.strip() == "":
                raise Empty("Address is empty")

            print("Order successfully placed")

        except (Unavailable,Fail,Empty) as e:
            print(e)


obj = Ecommerce()
obj.place_order()