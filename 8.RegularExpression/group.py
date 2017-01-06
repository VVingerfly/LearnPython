"""
A group can be created by surrounding part of a regular expression with parentheses.
This means that a group can be given as an argument to metacharacters such as * and ?.
"""
import re

print("_________________________ Test 1 _________________________")
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("match 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("match 2")

if re.match(pattern, "spam"):
    print("match 3")

if re.match(pattern, "egg2"):
    print("match 4")


print("_________________________ Test 2 _________________________")
pattern = r"a"
