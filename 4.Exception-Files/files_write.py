print("_________________________ Test 1 _________________________")
file = open("./files/file_write.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("./files/file_write.txt", "r")
print(file.read())
file.close()


print("_________________________ Test 2 _________________________")
# the write method returns the number of bytes written to a file, if successful.
msg = "Hello World!"
file = open("./files/file_write.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

print("_________________________ Test 3 _________________________")
