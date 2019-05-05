# variables must start with a letter or underscore

_cats = 1

# 2cats = 2 (this variable is named incorrectly)

# the rest of the name must consist of letters, numbers and underscores

cats2 = 2

# hey@you = 4 (this variable is named incorrectly)

# names are case sensitive

CATS2 = 200

CATS2 != cats2 # even though the variables appear to be named the same, they are different because one is all caps, the other is all lowercase

_Cats = 100

_Cats != _cats # even though the variables appear to be named the same, they are different because one starts with a capital letter, the other starts with a lowercase letter