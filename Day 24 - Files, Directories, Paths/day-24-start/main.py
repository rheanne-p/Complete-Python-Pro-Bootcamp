# TODO 1. Individual Methods
print("Individual Methods:")

# in-built method
# takes inputs: file, mode, etc...
# open file, save in variable
file = open("my_file.txt")

# read method
# returns contents of the txt file as a String
contents = file.read()
print(contents)

# close the file
# once python opens, it takes up computer resources
# may close on its own
file.close()


# TODO 2. With Keyword
print("With Keyword:")
# with keyword
# open file and open as a name
# keyword manages file directly, automatically closes file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# no longer need to close

# TODO 3. Write Mode
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
# error: io.UnsupportedOperation: not writable
# file opened in read only mode, must put mode in parameters list
# all previous text in txt file got deleted

# TODO 4. Create a new file
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
# creates a new file that doesn't currently exist when you call write mode



# mode w: write
# mode a: append