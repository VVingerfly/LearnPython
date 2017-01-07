"""
Extract email address from a string
"""

import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
# Our regex contains 3 groups:
# 1. first part if the email address
# 2. domain name without the suffix
# 3. the domain suffix
# [\w\.-]+ matches one or more word character, dot or dash
# the refex above says that the string should contain a word (with dots and dashed allowed),
# followed by the @ sign, then another similar word, then a dot and another word.

str1 = "Please contact info@sololearn.com for assistance"
str2 = "My email addresses are npulee@163.com and lw15@mail.ustc.edu.cn"

match = re.search(pattern, str1)
if match:
    print(match.group())

matchall = re.findall(pattern, str2)
if matchall:
    print(list(matchall))
