# Basic Import
# keyword module_name
import turtle
tim = turtle.Turtle()
# when using method once or twice

# from... import...
from turtle import Turtle
tom = Turtle()
# when using method more than twice

# from module import *
# * imports everything within the module
from turtle import *
forward(100)
# confusing, you don't know its origins

# Aliasing Moduels
# keyword module_name as alias name
import turtle as t
ten = t.Turtle()
# t represents the entire module name

# Installing Modules
import heroes
# error: "no module named heroes"
# turtle is packaged with the python standard library
# go to pypi.org, full of python packages

# hover over red line and click on red lightbulb
# red lightbulb introduces pop-up to install package



