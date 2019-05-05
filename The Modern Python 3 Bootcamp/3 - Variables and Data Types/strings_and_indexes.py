# indexes in a string can be used to call a character in a numeric position in a string

"lol"[0] # will return "l"
"lol"[1] # will return "o"
"lol"[2] # will return "l"
"lol"[3] # will return an "index out of range error"

# if you pass in negative numbers, they start from the end of the string

"yessir"[-1] # will return "r"
"yessir"[-3] # will return "s"