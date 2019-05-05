'''
what does the following loop do?
'''

i = 1
while i < 5:
    i + i
    print(i)

# it prints 1 forever

'''
what does the following loop do?
'''

# print 1 to 5
i = 0
while i <=5:
    i =+ 1
    print(i)

# it prints 1 forever because there is a type with the increment which should be += instead of =+

'''
what can we do to get out of the infinite loop below?
'''

# this code runs forever
x = 0
while x != 11:
    x += 2
    print(x)

# change the condition to x != 10
# change the condition to x < 11
# add logic that says if x == 10: break
# press control + c while your program is running to kill it

# all of the above