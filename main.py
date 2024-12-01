item1 ="Phone"
item1_price = 100
item1_quantity =5
item1_price_total = item1_price * item1_quantity

print(type(item1))
print(type(item1_quantity))
print(type(item1_price))
print(type(item1_price_total))


print("-----------------------------------------------")
class Item:   #class
    def __init__(self,name):
        # print(f"An instance created: {name}")
        pass
    def calculate_total_price(self,x,y):
        # return x*y
        return self.price * self.quantity
    
print(item1.calculate_total_price(item1.price, item1.quantity))

print("-----------------------------------------------")

item1 = Item("phone") #obj
#instance of class
item1.name = "phone"
item1.price= 20
item1_quantity= 100
print(item1.calculate_total_price(item1.price, item1.quantity))


item2 = Item("laptop")
item2.name = "laptop"
item2.price= 50
item2_quantity= 1000
print(item2.calculate_total_price(item2.price, item2.quantity))

print(type(item1))
print(type(item1_quantity))
print(type(item1_price))
print(type(item1_price_total))

print("-----------------------------------------------")

random_str = 'aaa'
print(random_str.upper())
print("-----------------------------------------------")

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)

item1 = Item("Phone", 100)
item2 = Item("Laptop",1000)

# item2.has_numpad =False
print("-----------------------------------------------")

