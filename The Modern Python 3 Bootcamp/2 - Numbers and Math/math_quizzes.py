# How can we add parenthesis to the following expression to make it equal 100?
# 1 + 9 * 10

print((1+9)*10) # putting the parenthesis around the 1+9 equations equals 10, which when multiplied by 10 = 100

# What is the result of the following expression?
# 2 + 10 * 5 + 3 * 2

print(58) # multiplications occur first in order of operation which changes the equation to 2 + 50 + 6, adding them together equals 58

# What is the result of the following expression?
# 6 * 8 / 2**3 - 2 * 2

print(2) # the exponentiation occurs first, 2**3=8, then multiplication - 6*8=48 and 2*2=4, changing the equation to 48 / 8 - 4. Division occurs, 48/8=6. Subtraction occurs, 6-4=2.

# What is the result of running the following code?
# 1/2 * 2 # + 1

print(1.0) # the comment prevents the latter half of the line from running, so we only see 1/2 * 2 which is 1.0. 1/2=0.5, which when multiplied by 2 equals 1

# Which of the following result in integers in Python?
# A. 6/2
# B. 5//2
# C. 6.5*2

print("B") # A will return a float since all equations using / return floats, C will return a float since a float is part of the equation (6.5)

# What is the result of 16 //6?

print(2) # 6 is only divisble by 16 twice

# What is the result of 111 % 7?

print(6) # This equation will return 6 - because there is a remainder of 6 after 111 is divided by 7 (15 times - 7*15=105, 111-105=6)