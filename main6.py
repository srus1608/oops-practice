#getters setters
from item import Item

item1 = Item("MyItem", 750)

# Setting an Attribute
item1.name = "OtherItem"

# Getting an Attribute
print(item1.name)


# @property 
# def name(Self):
#     return self.__name


# @name.setter
# def name(self, value):
#     print("You are trying to set")
#     self.__name =value

#if want to set exception
def name(self, value):
    if len(value)>10:
        raise Exception("this name is to long!")
    else:
        self.__name = value