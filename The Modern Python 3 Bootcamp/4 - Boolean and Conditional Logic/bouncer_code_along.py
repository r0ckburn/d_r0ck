# ask for age
age = input("How old are you? ")
if age:
    age = int(age)
    # 18 - 21 wristband
    if age >= 18 and age <21:
        print("You can enter, but need a wristband")
    # 21+ drink, normal entry
    elif age >= 21:
        print("You can enter and can drink")
    # too young, sorry
    else:
        print("You can't come in, little one ):")
else:
    print("Please enter an age")

# this could be rewritten as the following
# this is more efficient than the first example

# ask for age
age = input("How old are you? ")
if age:
    age = int(age)
    # 21 or older can come in and drink
    if age >= 21:
        print("You can enter and can drink")
    # 18-20 can come in but can't drink
    elif age >= 18:
        print("You can enter but cannot drink")
    # too young to come in
    else:
        print("You can't come in, little one ):")
else:
    print("Please enter an age")