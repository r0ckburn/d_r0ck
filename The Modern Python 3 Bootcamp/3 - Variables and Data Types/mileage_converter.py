print("How many kilometers do you want to convert to miles?")
kms = input() # the input method requires a user to provide a value before proceeding with the next step of the script
miles = float(kms)/1.60934 # declaring kilometers as a float to allow users to enter a float
miles = round(miles, 2) # rounding the number to the second decimal place
print(f"{kms} kilometers is equal to {miles} miles.")
