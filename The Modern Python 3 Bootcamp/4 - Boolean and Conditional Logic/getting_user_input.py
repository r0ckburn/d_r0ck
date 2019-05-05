# there is a built-in function in Python called "input" that will prompt the user and store the result to a variable

name = input("Enter your name here: ")
print(name)

# you can combine the variable that an end user input something to with a string

data = input("What's your favorite color?")
print("You said " + data)

# preferred to do a print statement first, then declare the variable and print the variable later -- this also puts the input on a separate line

print("What's your favorite color?")
data = input()
print("You said " + data)
