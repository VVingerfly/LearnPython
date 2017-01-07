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
# The content of groups in a match can be accessed using the group function.
# group(0) or group() returns the whole match.
# group(n) returns the nth group from the left(n>0)
# groups() returns all groups up from 1
# 
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())


print("_________________________ Test 3 _________________________")
# named groups: have the format (?P<name>...), where name is the name of group and ... is the content.
# They behave the same as normal groups, except they can be accessed by group(name) in addition to its number.
# Non-capturing groups: have the format (?:...), they are not accessible by the group method,
# so they can be added to an existing regular expression without breaking the numbering.
pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

print("_________________________ Test 3 _________________________")
# Another important metacharacter is |, which means "or"
# red|blue matches either "red" or "blue"

pattern = r"gr(a|e)y"
match = re.match(pattern, "gray")
if match:
    print("Match 1")

match = re.match(pattern, "grey")
if match:
    print("Match 2")

match = re.match(pattern, "griy")
if match:
    print("Match 3")


