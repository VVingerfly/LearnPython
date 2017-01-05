"""
Magic methods are special methods which have double underscores at the beginning and end of
their names. They are alse known as dunders. They are used to created functionalities that can'type
be represented as a normal method.
One common use of them is operator overloading. This means defining operators for custom classes
that allow operator such as + and * to be used on them.
+ __add__
- __sub__
* __mul__
/ __truediv__
// __floordiv__
% __mod__
** __pow__
& __and__
^ __xor__
| __or__
The expression x + y is translated into x.__add__(y). However, if x hasn't implemented __add__,
and x and y are of different type, then y.__radd__(x) is called. There are equivalent r methods
for all magic methods just mentioned.
"""

print("_________________________ Test 1 _________________________")
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second  = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)



print("_________________________ Test 2 _________________________")
# <  __lt__
# <= __le__
# == __eq__
# != __ne__
# >  __gt__
# >= __ge__
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs



print("_________________________ Test 3 _________________________")
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in
import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
    def __len__(self):
        return random.randint(0, len(self.cont)*2)


vague_list = VagueList(["A", "B", "C", "D","E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
print("end")
