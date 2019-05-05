'''
Repeat everything until the user says "stop copying me"
'''

msg = input("Say something: ")

while msg != "Stop copying me":
    print(msg)
    msg = input()
print("Ugh fine!")