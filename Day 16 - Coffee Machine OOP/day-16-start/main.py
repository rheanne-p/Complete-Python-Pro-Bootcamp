# TODO 1. Modules
import another_module

# value from another module used in main.py
print(another_module.another_variable)


# TODO 2. Classes
# tap into class called Turtle declared within turtle module
#    module        class   Screen: another class (within Turtle module)
from turtle import Turtle, Screen

# object = class (PascalCase)
timmy = Turtle()
# (parentheses) initializes / constructs object

# print object
timmy.shape("turtle")
timmy.shapesize(10)
timmy.color("aquamarine4")
timmy.forward(300)

#      shape: a method that changes the shape of the turtle
print(timmy)
# saved at 0x000001F752996080 location in computer


# TODO 3. Object Attributes
# data that can be kept track of, models real-life object


# create screen object
#           Screen() class: window in which turtle shows up
my_screen = Screen()


# from this my_screen object, get the "canvheight" attribute (variable)
# no parentheses after attribute name
# object . attribute
my_screen.canvheight
# canvas height is an attribute associated with the screen
# when printed, canvheight attribute's value is originally set to 300 in Screen() class
print(my_screen.canvheight)

# TODO 4. Object Methods
# functions associated with an object

# object  method
my_screen.exitonclick()
# exitonclick(): a method that keeps program running until screen is clicked

# you can pass in arguments in the parentheses to modify the attribute / method
