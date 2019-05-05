# comparison operators allow us to compare two different pieces of data

# here is a list of comparison operators
# in this example a == 1 and b = 1

# == - Truthy if a has the same value as b, e.g. a == b #True
# != - Truthy if a does NOT have the same value as B, e.g. a != b #False
# > - Truthy if a is greater than b, e.g. a > b #False
# < - Truthy if a is less than b, e.g. a < b #False
# >= - Truthy if a is greater than or equal to b, e.g. a >= b #True
# <= - Truthy if a is less than or equal to b, e.g. a <= b #True

# == is equal to

1 == 1 # True
1 == 2 # Fa;se
"a" == "A" #False

# != is not equal to

1 != 1 # False

color = "teal"
color != "purple" # True

# > and <

1 < 3 # True
-100 > -200 # True

# you shouldn't compare strings with > or < but it's possible

"A" > "a" # False
"A" < "a" # True
"b" > "a" # True

# >= and <=

age = 18
age >= 18 # True
age <= 6 # False

if age >= 18:
    print("You are an adult!")
