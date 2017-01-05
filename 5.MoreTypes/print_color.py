
# display text on a Windows console
# Windows XP with Python27 or Python32
from ctypes import windll
# needed for Python2/Python3 diff
try:
    input = raw_input
except:
    pass
STD_OUTPUT_HANDLE = -11
stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
# look at the output and select the color you want
# for instance hex E is yellow on black
# hex 1E is yellow on blue
# hex 2E is yellow on green and so on
for color in range(0, 75):
     windll.kernel32.SetConsoleTextAttribute(stdout_handle, color)
     print("%X --> %s" % (color, "Have a fine day!"))
    #  input("Press Enter to go on ... ")