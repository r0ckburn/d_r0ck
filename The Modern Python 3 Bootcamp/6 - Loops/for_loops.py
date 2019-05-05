# In python, for loops are written like this:

# for item in iterable object:
    # do something with item

# An iterable object is some kind of collection of items, for instance: a list of numbers, a string of characters, a range, etc.

# item is a new variable that can be called whatever you want

# item references the current position of our iteration within the iterable. It will iterate over (run through) every item of the collection and then go away when it has visited all items.

# e.g.

# list

list = [40,32,73]
for item in list:
    print(item)

# string

for letter in "coffee":
    print(letter)
    print(letter * 10)

# for loops with ranges

for x in range(1,10):
    print(x)
    print(x*x)