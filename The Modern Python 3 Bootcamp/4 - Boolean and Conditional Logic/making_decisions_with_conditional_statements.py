# Conditional Statements
# Conditional logic using if statements represents different paths a program can take based on some type of comparison of input

# if some condition is True:
#   do something
# elif some other condition is True:
#   do something
# else:
#   do something

# You need 1 if, can have as many elif's as you want, and you can only have 1 else
# the colons are important - they indicate an indented block will follow the statement
# indentation is important - you will receive an error if spacing is incorrect

# example

name = ""
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "John Snow":
    print("You know nothing")
else:
    print("Carry on")

# another example

color = input("What's your favorite color?")
if color == "Brown":
    print("Excellent Choice!")
elif color == "Pink":
    print("Gross!")
elif color == "Black":
    print("Are you a goth?")
else:
    print("Cool story!")