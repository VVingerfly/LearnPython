"""
Metacharacters are what make regular expressions more powerful than normal string methods.
"""
import re

print("_________________________ Test 1 _________________________")
# .(dot) matches any character, other than a new line.
pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

print("_________________________ Test 2 _________________________")
# ^ and $ match the start and end of a string, respectively.

pattern = r"^gr.y$" 
# ^gr.y$ means that the string should start with gr,
# then follow with any character, except a new, and end with y
if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stringray"):
    print("Match 3")
