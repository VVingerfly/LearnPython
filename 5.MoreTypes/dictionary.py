"""
Dictionary are data structures used to map arbitrary keys to values.
Each element in a dictionary is represented by a key:value pair.
Mutable objects can't be used as keys to dictionaries, such as lists, dictionaries.
"""

print("_________________________ Test 1 _________________________")
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Mary"])
print(ages["Dave"])

print("_________________________ Test 2 _________________________")
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}
print(primary["red"])
# print(primary["yellow"])  # return a KeyError

print("_________________________ Test 3 _________________________")
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

print("_________________________ Test 4 _________________________")
# use in and not in to determine whether a key is in a dictionary
nums = {
    1: "One",
    2: "Two",
    3: "Three",
}
print(1 in nums)
print("Three" in nums)
print(4 not in nums)

print("_________________________ Test 5 _________________________")
pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
print(fib.get(4, 5))
print(fib.get(8))
print(fib)

