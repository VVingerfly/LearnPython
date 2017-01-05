
myfile = open("./files/file1.txt")
myfile.close()

# read mode (default)
open("./files/file1.txt", "r")

# write mode
# when a file is opened in write mode, the file's existing content is deleted
open("./files/file1.txt", "w")

# append mode: add new content to the end of the file
open("./files/file1.txt", "a")

# binary write mode
# binary mode is used for non-text files (such as images and sound files)
open("./files/file1.txt", "wb")

print("Done!")
