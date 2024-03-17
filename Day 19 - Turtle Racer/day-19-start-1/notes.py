# Function in a Function
def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def calculator(n1, n2, function_name):
    return function_name(n1, n2)


result = calculator(2, 3, multiply)
print(result)

# Higher Order Functions: a function can work with other functions
# Calculator is a higher order function (takes another as input)
# Works for listening for events, and then triggering another function

# Use keyword arguments for other people's abstractions (methods)
