class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)        
    
# item = (Item.pay_rate)    
# item1 = (Item1.pay_rate)    
# item2 = (Item2.pay_rate)    

    
# item1 = Item("Phone", 100, -1)#asertion error
# item2 = Item("Laptop", 1000, -3)    

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

# print(Item.__dict__)# all attributes for class level
# print(item1.__dict__)#all instance for attribute level

print(item1.calculate_total_price())
print(item2.calculate_total_price())