"""
Functional programming is a style of programming that (as the name suggests)
is based around functions. A key part of functional programming is
high-order functions. High-order functions take other functions
as argument, or retutn them as results.
"""

print("_________________________ Test 1 _________________________")
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five, 10))


print("_________________________ Test 2 _________________________")
# Functional programming seeks to use pure functions.
# Pure functions have no side effects, and return the same result.
def pure_function(x, y):
    """
    Pure functions
    """
    temp = x + 2*y
    return temp / (2*x + y)

some_list = []
def impure(arg):
    """
    impure function
    """
    some_list.append(arg)

