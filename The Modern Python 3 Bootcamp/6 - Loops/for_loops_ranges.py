range(7)
# gives you integers from 0 thru 6 - count starts at 0 and is exclusive

range(1, 8)
# will give you integers from 1 to 7 - two parameters are (start,end)

range(1, 10, 2)
# will give you odds from 1 to 10 - third parameter is called the "step"
# meaning how many integers to skip

range(7, 0, -1)
# will give you integers from 7 to 1 - the negative number indicates to count
# down

# you can create a range like this:

range(10)  # this is a range for range(0,10)

# or you can create a variable which is a range

r = range(10)
list(r)

# or

nums = range(1, 10, 2)
list(nums)

# incorporating a for loop with a range

for num in range(10):
    print(num)

# or

for num in range(0, 105, 5):
    print(num)

x = range(10, 20, 3)
for x in range(10, 20, 3):
    print(x)
