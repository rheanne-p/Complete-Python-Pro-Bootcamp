# Unlimited Arguments
def add(*args):       # *args stands for arguments
    total = 0
    for n in args:    # loop through each argument (tuple)
        total += n    # manipulate each argument
    print(type(args))
    print("Argument at position 0: ")
    print(args[0])    # fetch argument using index
    return total


# Calling Function
print(add(3, 5, 7, 8))