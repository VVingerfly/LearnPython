"""
Methods of objects we've looked so far are called by an instance of a class,
which is then passed to the self parameter of the method.
"""

print("_________________________ Test 1 _________________________")
# Class methods are different - they are called by a class, which is passed to the cls parameter.
# A common use of these are factory methods, which instantiate an instance of a class,
# using different parameters than those usuallt passed to the class construtor.
# Class methods are marked with a classmethod decorator.
class Rectangle:
    def __init__(self, widht, height):
        self.width = widht
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    
    @classmethod
    def new_square(cls, side_length):
        """
        new_square is a class method and is called on the class, rather than on an instance of class
        It returns a new object of the class cls.
        """
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

print("_________________________ Test 2 _________________________")
# Static method are similar to class methods, except they don't receive any additonal arguments;
# they are identical to normal functions that belong to a class.
# They are marked with the staticmethod decorator.
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @staticmethod
    def validate_topping(topping):
        if topping == "Pineapple":
            raise ValueError("No pineapple!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
# static methods behave like plain functions, except for the face that
# you can call them from an instance of the class

