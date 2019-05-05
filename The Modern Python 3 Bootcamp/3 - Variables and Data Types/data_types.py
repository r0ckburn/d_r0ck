# in any assignment, the assigned value must always be a valid data type

# bool (boolean) = True or False values

True or False # must be capitalized in order for python to know it's a boolean. if lowercase is used, it would try to reassign the variable to another variable named 'true' or 'false'

is_active = True
print(is_active)

game_over = False
print(game_over)

# int (integer) = an integer (1,2,3)

age = 32

# str (string) = a sequence of Unicode characters, e.g. "David"

some_string = "8"
type(some_string) # will return <class> 'str'

some_string = "hello, I am a string"
type(some_string) # will still return <class> 'str'

# list (list)= an ordered sequence of values of other data types, e.g. [1,2,3] or ["a","b"."c"]

family = ["David", "Sara", "Indigo"]

# dict (dictionary) = a collection of key: values, e.g. {"first_name": "David", "last_name": "Rockburn"}

family_roles = {"Father": "David", "Mother": "Sara", "Daughter": "Indigo"}