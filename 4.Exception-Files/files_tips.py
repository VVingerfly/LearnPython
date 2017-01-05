
print("_________________________ Test 1 _________________________")
# It's a good practice to avoid wasting resources
# by making sure that files are alwsys closed after they have been used.
# One way of doing this is to use try and finally.
try:
    file = open("./files/file_read.txt", "r")
    print(file.read())
    # print(1 / 0)
finally:
    file.close()


print("_________________________ Test 2 _________________________")
# An alternateive way of doing this is using with statements.
# This creates a temporary variable (ofter called f),
# which is only accessiable in the indented block of the with statement.
with open("./files/file_read.txt", "r") as f:
    print(f.read())
