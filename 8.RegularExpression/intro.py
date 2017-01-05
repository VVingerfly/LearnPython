"""
Regular Expressions are a powerful tool for various kinds of string manipulation.
They are useful for two main tasks:
    - verifying that stirng match a pattern
    (for instance, that a string has the format of an email address)
    - performing substitutions in a string (such as changing all American spellings to British ones)
Regular Expressions in Python can be accessed using the re module, which is part of the standard lib
"""

print("_________________________ Test 1 _________________________")
# re.match function can be used to determine whether it matches at the beginning of a string
# If it does, match returns an object representing the match, if not, it returns None.
# To avoid any confusion while working with regular expressions, we would use raw strings
# as r"expression". Raw strings don't escape anything, which makes use of regular expressions easier
import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")


print("_________________________ Test 2 _________________________")
# re.search finds a match of a pattern anywhere in the string
# re.findall returns a list of all substrings that match a patten
# re.finditer dose the same thing as re.findall, except it returns an iterator, rather than a list
import re

pattern = r"spam"
if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))


print("_________________________ Test 3 _________________________")
# The regex search returns an object with several methods that give details about it.
# These methods include group which returns the string matched, start and end which the
# start and ending positions of the first match,
# and span which return the start and end positions of the first match as a tuple.
import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


print("_________________________ Test 4 _________________________")
# One of the most important re methods that use regular expressions is sub.
# re.sub(pattern, repl, string, max=0)
# This method replaces all occurrences of the pattern in string with repl,
# substituting all occurrences, unless max provided. This method returns the modified string.
import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

