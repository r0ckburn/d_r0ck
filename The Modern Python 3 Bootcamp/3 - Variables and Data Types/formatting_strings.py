# interpolation

# f strings
# allows you to format the string by using curly braces and putting a variable inside

x = 10
formatted = f"I've told you {x} times already!"
print(formatted) # I've told you 10 times already!

guess = 8
print(f"your guess of {guess} was incorrect") # your guess of 8 was incorrect

# you can also do some math inside of the curly braces

guess = 8
print(f"your guess of {guess + 1 } was incorrect") # your guess of 9 was incorrect

# you can also pass in two variables in a formatted string

name = "bluethecat"
guess_two = "10"
print(f"nice try, {name}, but your guess of {guess_two} was wrong!") # nice try, bluethecat, but you guess of 10 was wrong!

# in python versions before 3.6, f strings were not supported
# you enter the strings, and curly braces where the variables should be, but after the string you need to add ".format" and enter the sequence of the variables separated by a comma
# e.g.

fruit = "banana"
ripeness = "unripe"
print("The {} is {}.".format(fruit, ripeness))