import json

f = open("Input Files\Birthday.json", 'r')
f = json.load(f)

print('Welcome to the birthday dictionary. We know the birthdays of:')
for a in f:
    print(a)
name = input("Who's birthday do you want to look up?\n")
print(name + "'s b'day is on : " + f[name])
res = input("press 'y' to add a new b'day or any key to exit.\n")
if res is 'y':
    add = dict(input('Add in the format: "Name" + : + "Bday(separated by /)"\n'))
    f = open("Input Files\Birthday.json", 'w')
    f = json.dump(add, f)
    f = open("Input Files\Birthday.json", 'r')
    f = json.load(f)
    print(f)
else:
    pass
