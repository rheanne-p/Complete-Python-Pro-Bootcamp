from prettytable import PrettyTable

# TODO 1. Create a PrettyTable object and save it to a variable called table
# obj = class (construction)
table = PrettyTable()
print(f"\nTODO 1: \n{table}")


# TODO 2. Use the add_column method to create a table of Pokemon names and types
# obj.method     field name (str) list of all data under column
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(f"\nTODO 2: \n{table}")

# add_column method takes in two inputs
# input 1: name of field
# input 2: list of strings for data

# TODO 3. Change the table style by tapping into the left-aligned attribute
# change appearance of table: controlled by an attribute (variable)
# attributes are titled as "f", which stands for "field"

print(f"Original Alignment: {table.align}")
# prints 'c', stands for 'centre alignment'

# change a variable by using =
# obj.attribute = "new alignment attribute"
table.align = "l"
print(f"\nTODO 3: \n{table}")
print(f"New Alignment: {table.align}")

# TODO Bonus 1: Change another method
# from  module   import  class??, not sure what MSWORD_FRIENDLY is
from prettytable import MSWORD_FRIENDLY
table.set_style(MSWORD_FRIENDLY)
print(type(MSWORD_FRIENDLY))
print(f"\nTODO Bonus 1: \n{table}")

# TODO Bonus 2: Change another attribute
table.border = False
print(f"\nTODO Bonus 2: \n{table}")