"""
Special sequences are written as a backslash followed by another character.

"""
import re

print("_________________________ Test 1 _________________________")
# A abckslash and a number between 0 and 99
# This matches the expression of the group of that number.

pattern = r"(.+) \1"
# Note that "(.+) \1" is not the same as "(.+) (.+)",
# because \1 refers to the first group's subexpression,
# which is the matched expression itself, and not the regex pattern.

if re.match(pattern, "word word"):
    print("match 1")

if re.match(pattern, "?! ?!"):
    print("match 2")

if re.match(pattern, "abc cde"):
    print("match 3")




print("_________________________ Test 2 _________________________")
# \d, \s, \w match digits, whitespace, and word characters respectively.
# In ASCII mode they equivalent to [0-9], [\t\n\r\f\v] and [a-zA-Z0-9_].
# In Unicode mode, they match certain other characters, as well. e.g., \w matches letters with accents.
# \D, \S, \W mean the opposite to the lower-case versions. e.g., \D matches anything that isn't a digit.

pattern = r"(\D+\d)"
# (\D+\d) matches one or more non-digits followed by a digit

if re.match(pattern, "Hi 999!"):
    print("Match 1")

if re.match(pattern, "1, 23, 456!"):
    print("match 2")

if re.match(pattern, " ! $?"):
    print("match 3")

print("_________________________ Test 3 _________________________")
# \A and \Z match the beginning and end of a string, respectively.
# \b matches the empty string between \w and \W characters, or \w characters and the beginning or end
# of the string. Informally, ot represents the boundary between words.
# \B matches the empty string anywhere else.

pattern = r"\b(cat)\b"
# "\b(cat)\b" matches the word "cat" surrounded by word boundaries

if re.search(pattern, "The cat sat!"):
    print("Match 1")

if re.search(pattern, "We s>cat<tered?"):
    print("match 2")

if re.search(pattern, "We scattered."):
    print("match 3")


print("_________________________ Test 4 _________________________")

pattern = r"\AS...\b.\Z"
if re.search(pattern, "SPAM!"):
    print("Match")
