'''
Print the following beautiful art(emojis increasing in number by 1 per line until there are 10 emojis on the bottom line) using both a for loops and a while loop:
print("\U0001f600")
'''
# for loop version

for num in range (1,11):
    print("\U0001f600" * num)

# while loops version

times = 1
while times <11:
    print("\U0001f600" * times)
    times += 1

# nested loop version

for x in range (3):
    for num in range(1, 11):
        print("\U0001f600" * num)

# weird nested loop without string multiplication

for num in range(1, 11):
    count = 1
    smileys = ""
    while count <= num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)

# Make a different shape with emojies

times = 1
while times < 20:
    print("\U0001f600" * times)
    times += 2