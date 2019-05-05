# in python, == and is are very similar comparators, but they are not the same

a = 1
a == 1 # True
a is 1 # True

# in the following example using lists
# == checks the values to see if they are the same
# is checks if a and b are stored in the same place in memory

a = [1, 2, 3] # a list of numbers
b = [1, 2, 3]
a == b # True
a is b # False because a and b are separate objects in memory

# another example

c = b
b is c # True because b and c are pointing to the same list in memory