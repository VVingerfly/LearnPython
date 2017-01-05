"""
Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method, which means when an indtance
attribute with the same name as the method is accessed, the method will be called instead.
"""

print("_________________________ Test 1 _________________________")
# One common use of a property is to make an attribute read-only.
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True

print("_________________________ Test 2 _________________________")
# Properties can also be set by defining setter/getter functions.
# The setter function sets the corresponding property's valuse.
# The getter gets the value.
# To define setter/getter, you need to use a decorator of the same name as the property,
# followed by a dot and the setter/getter keyword.
class Cake:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            # password = input("Enter the password: ")
            password = "Hi"
            if password == "Hi":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

cake = Cake(["cheese", "tomato"])
print(cake.pineapple_allowed)
cake.pineapple_allowed = True
print(cake.pineapple_allowed)
