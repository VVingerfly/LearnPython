"""
Functional programming is a style of programming that (as the name suggests)
is based around functions. A key part of functional programming is
high-order functions. High-order functions take other functions
as argument, or retutn them as results.
"""

print("_________________________ Test 1 _________________________")
# map: takes a function and itereble as arguments, and returns a new
# iterable with the function applied to each argument.
def add_five(x):
    return x+5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

result = list(map(lambda x: x+5, nums))
print(result)

# filter: filters an iterable by moving items that don't match a predictable,
# a function that returns a Boolean
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)



print("_________________________ Test 2 _________________________")
# generator: a type of iterable, like lists or tuples.
# unlike list, they don't allow indexing with arbitrary indices,
# but they can still be iterated through with for loops.
# they can be created using functions and the yeild statement.
# the yield statement is used to define a generator， replacing the return
# of a function to provide a result to its caller without destroying local variables.
#
# Using generators results in improved performance, which is the result of the lazy (on demand)
# generation of values, which translates to lower memory usage. Furthermore, we do not need to wait
# until all the elements have been generated before we start to use them.
def countdown():
    i = 5
    while i > 0:
        yield i  
        i -= 1
for i in countdown():
    print(i)

# Due to the fact that they yield one item at a time, generators don't have
# the momory restrictions of lists.
# In fact, they can be infinite!
# def infinite_sevens():
#     while True:
#         yield 7
# for i in infinite_sevens():
#     print(i)


# Finete generators can be converted into lists by passing them as arguments to the list function.
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))



print("_________________________ Test 3 _________________________")
# Decoretors: provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions
# that you don't want to modify.
def decor(func):
    def warp():
        print("=============")
        func()
        print("=============")
    return warp

def print_text():
    print("Hello World!")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()


# Python provides support to warp a function in a decorator by pre-pending the function definition
# with a decorator name and the @ symbol.
@decor
def print_text_decor():
    print("Hello World!!!")

print_text_decor()


print("_________________________ Test 3 _________________________")
# Recursion: 
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))


print("_________________________ Test 4 _________________________")
# Set: data structures, similiar to lists or dictionaries.
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sauage"])

print(3 in num_set)
print("spam" not in word_set)

empty_set = set()
print(empty_set)


nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)  # union: combine two sets to from a new one containing items in either
print(first & second)  # intersection: get items only in both
print(first - second)  # difference: get items in first set but not in the second
print(second - first)
print(first ^ second)  # symetric difference: get items in either set, but not both


# Python support lists, dicnaries, tuples, sets
# When to use a dictionary:
#   - when you need a logical association between a key:value pair
#   - when you need fast lookup for your data, based on a custom Key
#   - when your data is being constantly modified. Remember, dictionaries are mutable.
# When to use the other types:
#   - use lists if you have a collection of data that does not need random access.
#     try to choose lists when you need simple, iterable collection that is modified frequently.
#   - use a set if you need uniqueness for the elements
#   - use tuples when your data cannot change.
