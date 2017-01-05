
def hello():
    print("Hello World!")

hello()

def sum(x, y):
    print(x + y)

sum(3, 5)


def max(x, y):
    """ 
    docstrings: return the maximum of two numbers
    """
    if x>= y:
        return x
    else:
        return y

z = max(3,6)
print(z)

 # functions can be assigned and reassigned to variables
max_copy = max 
print(max_copy(3, 6))

# functions can be used as arguments of other functions
def add(x, y):
    return x + y

def add_twice(func, x, y):
    return func(func(x, y), func(x, y))

print("add twice: ", add_twice(add, 3, 4))

