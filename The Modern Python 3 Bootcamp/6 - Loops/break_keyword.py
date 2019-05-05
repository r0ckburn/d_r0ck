'''
the keyword break gives us the ability to exit out of the loop whenever we want
'''

# example using a while loop

while True:
    command = input("Type 'exit' to exit: ")
    if (command == "exit"):
        break

# example using a for loop

for x in range (1,101):
    print(x)
    if x == 3:
        break

# an example using the for loop "clean up your room" exercise

times = int(input("How many times do I have to tell you? "))

for time in range(times):
    print("Clean up your room!")
    if time >= 4:
        print("Do you even listen anymore?")
        break
