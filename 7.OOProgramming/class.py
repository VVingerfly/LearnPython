"""
__init__ is the most important method in a class. 
This is called when an instance (object) of the class is created.
All method must have 'self' as their first parameter, although it isn't explicitly passed.
Instances of a class have 'attribute', like color, legs in the following example.

"""

print("_________________________ Test 1 _________________________")
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
print(felix.color)

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()


print("_________________________ Test 2 _________________________")

