# string concatenation is when you combine multiple strings together
# in python you do this with the "+" operator

str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two
print(str_three) 
# your face

username = "bluethecat"
print("Hello there and welcome to the game, " + username + "!") # Hello there and welcome to the game, bluethecat!

"a" + "b" + "c" # abc

# you can't combine a numeric character and an alphanumeric string

print(8 + "hello") # this will result in an error since 8 is an int and "hello" is a string

# you can also use the += operator to combine strings for the same variable - handy instead of creating multiple variables and adding them together

str_four = "ice"
str_four += " cream"
print(str_four) # ice cream

# or

str_five = "ice"
str_six = " cream"
str_seven = str_five + str_six 
print(str_seven) # ice cream

# this also works with numeric values

str_eight = 99
str_eight += 1
print(str_eight) #100

# This works with other mathematical equations as well 

str_nine = 100
str_nine -= 10
print(str_nine) # 90

str_ten = 100
str_ten /= 10
print(str_ten) # 10

str_eleven = 10
str_eleven *= 20
print(str_eleven) # 200