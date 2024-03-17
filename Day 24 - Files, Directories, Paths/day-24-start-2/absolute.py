with open("/Users/Rheanne/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("/Users/Rheanne/Desktop/new_file.txt", mode="w") as file:
    file.write("I have created a new file.")

# Creates a new txt file in the specified file path
with open("/Users/Rheanne/Desktop/new_file.txt", mode="r") as file:
    new_contents = file.read()
    print(new_contents)

print("Running Absolute!")
