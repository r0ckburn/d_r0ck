# What is truthiness?
# 1 - Statements or facts that seem "kind of true" even if they are not necessarily true.
# 2 - Statements or expressions that resolve to a True value.
# 3 - Code that never lies passes the "truthiness" test.
# 4 - Computers have a tendency to assume things are true until proven False.

print("2 - Statements or expressions that resolve to a True value.")

# Is the following expression truthy or falsy?
# truthy (x has a non-falsy value)
# falsy (y has a falsy value)

x = 15
y = 0
x or y # this expression

print("truthy (x has a non-falsy value") # if one of x or y is truthy, then the or statement will always be truthy

# Is the following expression truthy or falsy?
# truthy, because x has a value
# falsy, because 0 and None are both falsy values

x = 0
y = None
x or y # this expression

print("falsy, because 0 and None are both falsy values") # the expression becomes something like "False or False"

# Is the following expression truthy or falsy?
# truthy, b has a truthy value therefore a and b must be truthy
# falsy, because a is 0 which is a falsy value

a = 0
b = 1000
a and b # this expression

print("falsy, because a is 0 which is a falsy value") # both a AND b have to be truthy

# Is the following expression truthy or falsy?

a = -1
not a # this expression

print("falsy") # negative numbers are just like regular numbers, so not (True) is false

# Is the following truthy or falsy?

x = 0
y = -1
x or y and x - 1 == y and y + 1 == x 

print("truthy") # (x or y) is truthy because y is -1 which is a nonzero value; (x - 1 == y) is truthy because x - 1 is -1, and -1 == -1; and (y + 1 == x) is truthy because -1 + 1 = 0, and 0 ==0.