# Problem 6: E-Commerce Discount Calculator
# An online store gives discounts based on cart value: Above ₹5000 → 25%; Above
# ₹3000 → 15%; Above ₹1000 → 10%; Otherwise no discount. Extra Rules: Premium
# members get additional 5%; GST = 18%. Display final payable amount.
# Concepts: Operators, Nested conditions, Typecasting, Arithmetic calculations
# Sample Input:
# Cart value: 6000
# Premium member: yes
# Sample Output:
# Discount Applied = 1800
# GST = 756
# Final Amount = 4956

# Source Code:

# Input
cart_value = float(input("Cart value: "))
premium_input = input("Premium member: ").lower()

# Determine base discount rate using nested conditions
if cart_value > 5000:
    discount_rate = 25
elif cart_value > 3000:
    discount_rate = 15
elif cart_value > 1000:
    discount_rate = 10
else:
    discount_rate = 0

# Extra 5% for premium members
if premium_input == "yes":
    discount_rate += 5

# Arithmetic calculations
discount = cart_value * discount_rate / 100
amount_after_discount = cart_value - discount
gst = amount_after_discount * 18 / 100
final_amount = amount_after_discount + gst

# Output with typecasting to int for clean display
print(f"Discount Applied = {int(discount)}")
print(f"GST = {int(gst)}")
print(f"Final Amount = {int(final_amount)}")