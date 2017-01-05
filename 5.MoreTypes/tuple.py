"""
Tuples are veru similar to losts, except that they are immutable (they cannot be changed)
[] list
{} dictionary
() tuple
"""

print("_________________________ Test 1 _________________________")
words = ("spam", "eggs", "sausages",)
print(words[0])
# words[1] = "cheese" # return a TypeError

print("_________________________ Test 2 _________________________")
my_tuple = "one", "two", "three"
print(my_tuple[1])
