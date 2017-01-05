"""
"""

print("String formatting")
print("_________________________ Test 1 _________________________")
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)

a = "{x}, {y}, {x}".format(x=5, y=12)
print(a)

print("String functions")
# join: joints a list of strings with anotherstring as a separator
# split: the opposite of join, turn a string eith a certain separator into a list
# replace
# startswith & endswith
# upper & lower
print("_________________________ Test 2 _________________________")
print(", ".join(["spam", "eggs", "ham"]))

print("spam, eggs, ham".split(", "))

print("Hello ME".replace("ME", "world"))

print("This is a sentence.".startswith("This"))

print("This is a sentence.".endswith("This"))

print("This Is A Sentence.".upper())

print("This Is A Sentence.".lower())

