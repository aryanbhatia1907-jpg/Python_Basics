class Pizza:
    def __init__(self,name,size,price):
        self.name =name
        self.size = size
        self.price = price

    @classmethod
    def from_string(cls, pizza_str): 
        parts=pizza_str.split("-")
        return cls(parts[0], parts[1], int(parts[2]))
    
    @classmethod
    def from_dict(cls, pizza_dict):
        return cls(pizza_dict["name"], pizza_dict["size"], pizza_dict["price"])
    
    def __str__(self):
        return f"Pizza: {self.name} | Size: {self.size} | Price: Rs.{self.price}"
    
p1 = Pizza("Farmhouse", "Large", 350)
p2 = Pizza.from_string("Margherita-Medium-250")
p3 = Pizza.from_dict({"name": "Pepperoni", "size": "Small", "price": 199},)

print(p1)    # __str__ automatically call hoga!
print(p2)
print(p3)
