"""
Inheritance provides a way to share functionality between classes.

"""

print("_________________________ Test 1 _________________________")
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")

class Sheep(Animal):
    def bark(self):
        print("Mie...")

fido = Sheep("Fido", "brown")
print(fido.name)
fido.bark()


print("_________________________ Test 2 _________________________")
# if a class inherits from another with the same attributes or methods, it overrides them.

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof...")

huskt = Dog("Max", "grey")
print(huskt.name)
huskt.bark()


print("_________________________ Test 3 _________________________")
# The function super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's supeclass.

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()  # calls the spam method of the superclass

B().spam()
