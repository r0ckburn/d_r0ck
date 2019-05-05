times = input("How many times do I have to tell you? ")
times = int(times) # need to convert the string to an integer

for time in range(times):
    print("Clean up your room!")
    # you could also use an f string to format the print for each time
    # e.g.
    print(f"Time {time+1}: Clean up your room!") # the +1 will allow the print response to start with 1 instead of 0