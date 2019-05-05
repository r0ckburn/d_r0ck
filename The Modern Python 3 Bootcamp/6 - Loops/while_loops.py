'''
While loop example - "what's the secret password?"
'''

msg = input("What's the secret password?")
while msg != "bananas":
    print("WRONG!")
    msg = input("What's the secret password?")
print("CORRECT!")

'''
A simple for loop calling to list a range of numbers could be different in a while loop. Genereally prefer for loops for instances where you need a set number of loops since they're shorter. However, while loops can be more flexible.
'''

for num in range (1,11):
    print(num)

'''
This will cause an infinite loop! It will print 1 repeatedly until forcing the application to stop.
'''

num = 1
while num < 11:
    print(num)

'''
fix this by:
'''

num = 1
while num < 11:
    print(num)
    num += 1  # could also increment by 2's, 3's, etc.