# Conditional Statements example solution:

# example 1

from random import randint
choice = randint(1, 10)
print(choice) # I am only printing so I can see the number to verify the code is working as expected

if choice == 7:
    print("lucky")
else:
    print("unlucky")

# example 2 

from random import randint
num = randint(1, 1000)
print(num) # I am only printing so I can see the number to verify the code is working as expected

if num %2 != 0: # if number is not divisible by 2
    print("odd")
else:
    print("even")