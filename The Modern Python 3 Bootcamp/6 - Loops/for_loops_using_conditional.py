# this solution loops over all the numbers between 10 and 20,
# checking to see if the number is even inside the loop

x = 0

for n in range(10, 21):
    if n % 2 != 0:
        x += n

# instead of looping over every number between 10 and 20,
# this solution only loops over the odd numbers.

x = 0

for i in range(11, 21, 2):
    x += i
