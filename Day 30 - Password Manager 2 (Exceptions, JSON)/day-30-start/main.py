# File Not Found
with open("a_file.txt") as file:
    file.read()

# Key Error
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# Index Error
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

# Type Error
text = "abc"
print(text + 5)

# Catching Exceptions
# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were exceptions
# finally: do this no matter what happens
