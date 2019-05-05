# in python, all conditional checks resolve to True or False

x = 1
x is 1 # true
x is 0 # false

# we can call values that will resolve to True "truthy"
# or we can call values that will resolve to False "falsy"

# besides False conditional checks, other things that are naturally falsy include: 
# empty objects, empty strings, None, and zero.

# example 1

if 0: # this will only run if this statement is true
    print("yay!")

if 1: # this will run because "1" is truthy
    print("yay?")

# example 2

animal = input("enter your favorite animal")
print(animal + " is my favorite animal too!")

# there is a case where someone could not enter an animal, so we want to add a conditional statement to ensure input is provided

animal = input("enter your favorite animal")

if animal: # this checks to see if any input is provided
    print(animal + " is my favorite animal too!")
else: # this is run if nothing is entered
    print("you didn't enter an animal")
