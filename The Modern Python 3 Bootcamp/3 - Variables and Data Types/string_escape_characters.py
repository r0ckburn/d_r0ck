# Escape characters are metacharacters - they get interpreted by python to do something special
# They all start with a backslash

# \newline - backslash and newline ignored
# \\ - Backslash (\)
# \' - Single Quote (')
# \" - Double Quote (")
# \a - ASCII Bell (BEL)
# \b - ASCII Backspace (BS)
# \f - ASCII Formfeed (FF)
# \n - ASCII Linefeed (LF)
# \r - ASCII Carriage Return (CR)
# \t - ASCII Horizontal Tab (TAB)
# \v - ASCII Vertical Tab (VT)
# \ooo - Character with octal value 000
# \xhh - Character with hex value hh

# Escape sequences only recognized in string literals are:

# \N(name) - Character named 'name' in the Unicode database
# \uxxxx - Character with 16-bit hex value xxxx
# \Uxxxxxxxx - Character with 32-bit hex value xxxxxxxx

new_line = "hello\nworld" # this will create a new line after the escape sequence
print(new_line)
#hello
#world

str = "this is a backslash: \\"
print(str)
# This is a backslash: \

another_string ="hel\blo"
print(another_string)
# helo

yet_another_string = "he said \"ha ha\""
print(yet_another_string)
# he said "haha"