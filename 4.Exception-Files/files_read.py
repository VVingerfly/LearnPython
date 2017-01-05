
print("_________________________ Test 1 _________________________")
file = open("./files/file_read.txt", "r")
cont = file.read()
print(cont)
file.close()

print("_________________________ Test 2 _________________________")
file = open("./files/file_read.txt", "r")
print(file.read(4))   # read 4 byte from file
print(file.read(8))
print(file.read(4))
print(file.read())    # read the rest of the file
file.close()


print("_________________________ Test 3 _________________________")
# after all contents in a file have been read,
# any attempts to read further from that file will return an empty string,
# because you are trying to read from the end of the file.
file = open("./files/file_read.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()


print("_________________________ Test 4 _________________________")
file = open("./files/file_read.txt", "r")
print(file.readlines())
file.close()


print("_________________________ Test 5 _________________________")
file = open("./files/file_read.txt", "r")
for line in file:
    print(line)
file.close()
