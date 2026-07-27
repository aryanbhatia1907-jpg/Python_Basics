class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        items_str = ", ".join(self.items)
        return f"Cart has {len(self.items)} items: {items_str}"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        return new_cart

    def __contains__(self, item):
        return item in self.items


cart1 = ShoppingCart()
cart1.add_item("Apple")
cart1.add_item("Bread")

cart2 = ShoppingCart()
cart2.add_item("Milk")
cart2.add_item("Eggs")

print(cart1)
print(len(cart1))
print("Apple" in cart1)
print("Pizza" in cart1)

cart3 = cart1 + cart2
print(cart3)
print(len(cart3))