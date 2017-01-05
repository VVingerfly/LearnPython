"""
Character class provides a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.
"""
import re

print("_________________________ Test 1 _________________________")

pattern = r"[aeiou]"
# the pattern [aeiou] in the search function matches all strings
# that contain any one of the characters defined.
if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")

print("_________________________ Test 2 _________________________")
# class [a-z] matches any lowercase alphabetic character.
# class [G-P] matches any uppercase character from G to P
# class [0-9] matches any digit
# multiple ranges can be includes in one class.
# For example, [A-Za-z] matches a letter of any case.

pattern = r"[A-Z][A-Z][0-9]" 
# The pattern matches strings that contain two alphabetic uppercase letters followed by a digit.
if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")

print("_________________________ Test 3 _________________________")
# Place a ^ at the start of a character class to invert it.
# This causes it to match any characte other than the ones included.
# ^ has no meaning unless it is the first cahracter in a class.

pattern = r"[^A-Z]"
# the pattern [^A-Z] excludea uppercase strings
# Note that the ^ should be inside the brackets to invert the character class.
if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")



print("_________________________ Test 4 _________________________")
# Metacharacter * means "zero or more repetitions of the previous thing". It tries to match
# as many repetitions as possible. The "previous thing" can be a single character, a class,
# or a group of characters in "parentheses".

pattern = r"egg(spam)*"
# the pattern match strings that start with "egg" and follow with zero or more "spam"s.
if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")


print("_________________________ Test 5 _________________________")
# Metacharacter + is very similar to *, except it means "one or more repetitions",
# as opposed to "zero or more repetitions".

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "ggggggggggggggg"):
    print("Match 2")

if re.match(pattern, "abc"):
    print("Match 3")


print("_________________________ Test 6 _________________________")
# Metacharacter ? means "zero or one repetitions",

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")

if re.match(pattern, "icecream"):
    print("Match 2")

if re.match(pattern, "ice--ice"):
    print("Match 3")


print("_________________________ Test 7 _________________________")
# Metacharacter {} can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something". Hence {0,1} is the same as ?.
# If the first number is missing, it is taken to be zero.
# If the second number is missing, it is taken to be infinitely.

pattern = r"9{1,3}$"
# "9{1,3}$" matches string that have 1 to 3 nines.

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "99"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")