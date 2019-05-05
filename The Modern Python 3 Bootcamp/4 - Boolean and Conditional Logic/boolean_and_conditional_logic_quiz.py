# What does the following code do?

# if am_hungry:
#     print("get food")
# else:
#     print("go learn Python")

# 1 - Prints "get food" followed by "go learn Python"
# 2 - If am_hunry is truthy, it prints "get food" followed by "go learn Python"
# 3 - If am_hungry has been assigned a value, it prints "get food" otherwise it prints "go learn Python"
# 4 - Prints "get food" if am_hungry holds a truthy value, otherwise it prints "go learn Python"

print("4 - Prints 'get food' if am_hungry holds a truthy value, otherwise it prints 'go learn Python'") # the "go learn Python" branch only executes if am_hungry is falsy

# What does the following Python code do?

# if not x or y:
#     print("winter is coming")
# else:
#     print("valar morghulis")

# 1 - if x is falsy or y is falsy, print "winter is coming". otherwise print "valar morghulis"
# 2 - if x is falsy or y is truthy, print "winter is coming", otherwise print "valar morghulis"
# 3 - if x or y do not exist, print "winter is coming", otherwise print "valar morghulis"

print("2 - if x is falsy or y is truthy, print 'winter is coming', otherwise print 'valar morghulis'")

# What does the following python code do?

x = True

if x:
    x = False

elif not x:
    x = True

# 1 - Sets x to True, then sets x to False
# 2 - Sets x to True, then set x to False, then set x to True

print("1 - Sets x to True, then sets x to False")