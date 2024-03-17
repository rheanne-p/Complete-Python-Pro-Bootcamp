# File Not Found - Catching Exceptions

try:  # try running this line
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["qwerty"])
    # line should give key error, but doesn't
    # because of except
except FileNotFoundError:  # do this if there was an exception
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:  # get hold of error message
    print(f"The key {error_message} does not exist.")
# do not leave bare except
# executes body despite all different errors
else:  # executes when try works
    content = file.read()
    print(content)
finally:  # code that will unconditionally run
    file.close()
    print("File was closed.")
    raise KeyError("This is an error I made up.")
    # make error happen(specify message)
