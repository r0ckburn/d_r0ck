# loop through nums 1-20
# for 4 and 13, print "x is unlucky"
# for odd nums, print "x is odd"
# should look like:
# 1 is odd
# 2 is even
# 3 is odd
# 4 is unlucky

# for num in range(1, 21):
#     # this needs to be first so that 4 and 13 are only labeled unlucky
#     if num == 4 or num == 13:
#         print(f"{num} is UNLUCKY!")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# or to reduce the amount of prints:

for num in range(1, 21):
    # this needs to be first so that 4 and 13 are only labeled unlucky
    if num == 4 or num == 13:
        state = "UNLUCKY!"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")
