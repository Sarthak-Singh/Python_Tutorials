bdays = {'Albert Einstien': '14/3/1879',
         'Benjamin Franklin': '01/17/1706',
         'Stephen Hawking': '8/1/1942',
         'Isaac Newton': '4/1/1643'}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for a in bdays:
    print(a)
name = input("Who's birthday do you want to look up?\n")
print(name + "'s b'day is on : " + bdays[name])
