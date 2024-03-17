# Keyword Arguments

def calculate(n, **kwargs):  # **kwargs: unlimited keyword arguments
    print(type(kwargs))   # kwargs in form of dictionary
    print(kwargs)         # prints args as a dictionary
    print(kwargs["add"])  # retrieve value via keyword
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# Calling Function
calculate(2, add=3, multiply=5)