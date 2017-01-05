"""
A key part of object-oriented programming is encapsulation.

"""

print("_________________________ Test 1 _________________________")
# Weakly private methods and attributes have a single underscore at the beginning.
# This signals that they are private, and shouldn't be used by external code. However,
# it is mostly only a convention, and does not stop external code from accessing them.
# Its only actual effect is that "from module_name import *" won't import variables
# that start with a single underscore.
class Queue:
    def __init__(self, contnets):
        self._hiddenlist = list(contnets)
    
    def push(self, value):
        self._hiddenlist.insert(0, value)
    
    def pop(self):
        return self._hiddenlist.pop(-1)
    
    def __repr__(self):
        """
        __repr__ magic method is used for string representation of the instance
        """
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist) # _hiddenlist can still be accessed in the outside code.


print("_________________________ Test 2 _________________________")
# Strongly private methods and attributes have a double underscore at the beginningof their names.
# This causes theor names to be mangled, which means that they can't be accessed from outside class.
# The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are
# subclass that have methods or attributes with the same names.
# Name mangles methods can still be accessed externally, but by a different name.
# The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
# Basically, Python protects those members by internally changing the name to include class name.
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg)
print("end.")

