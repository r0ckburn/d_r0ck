# in python, the following operators can be used to make Boolean logic comparisons or statements
# and - Truthy if both a AND b are true (logical conjunction), e.g. if a and b: print(c)
# or - Truthy if either a OR b are true (logical disjunction), e.g. if am_tired or is_bedtime: print("go to sleep")
# not - Truthy if the opposite of a is true (logical negation), e.g. if not is_weekend: print("go to work")

# and example

age = 6

if age > 2 and age < 8 : # 6 is greater than 2, and less than 6
    print("You pay the child price!")

# or examples

print("Where do you live?")
city = input()

if city == ("Cleveland") or ("Ohio"):
    print("Hello, fellow Ohio resident!")
else:
    print("Cleveland rocks!")

# another or example

1 < 3 or 1 == 99 # one is true (1 < 3) so True will be returned

1 < 3 and 1 == 99 # both are not true, so False will be returned

# not examples

age = 10
age < 4 # False
not age < 4  # True

# another not example

# movie tickets based on age:

age = 3
# ages 0-8 $2 ticket
# ages 65+ $5 ticket
# ages 9-64 $10 ticket

if not((age >= 0 and age <= 8) or age >= 65):
    print("You pay $10 and are not a child or senior!")
elif age >= 65:
    print("You are a senior! Give me $5!")
else:
    print("You are a child! Pay me $2!")