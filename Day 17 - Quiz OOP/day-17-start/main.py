# Creating a Class
class User:
    """A blueprint to represent what our
    users have and can do on our website."""
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # id object gets set to the parameter user_id that gets passed in
        # parameter user_id gets manually set during initialization within parentheses

# Creating an Object
user_1 = User()
# parentheses initializes the object
# use PascalCase to name classes
# camelCase capitalizes all subsequent first letters, EXCEPT first word

# Adding Attributes to an Object
# attribute: variable associated with an object
user_1.id = "001"
user_1.username = "angela"
# tap into object, then add an attribute using dot (.) notation

print(user_1.username)

# Constructor
# part of the blueprint that allows us to specify what should happen
# when our object is being constructed
# known as initializing an object
# set variables to their starting values

class Car:
    def __init__(self):
# __ means special method with special function, (e.g., initializing attributes)
# creates starting values for attributes below
# __init__ function is called everytime you create a new object of this class
# each construction triggers the print statement under the __init__ function

# Constructing Attributes
class Car:
    def __init__(self, seats):
        self.seats = 5

# self: actual object being created / initialized (Car)
# add other parameters after comma
# parameter passed in when object is constructed from this class
# use parameter data to set object's attribute (line 3)

my_car = Car(5)
# same as:
my_car.seats = 5