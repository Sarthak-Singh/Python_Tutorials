word = input('Enter a garbage value:\n')
lower = 0
upper = 0
num = 0
cht = 0
for x in word:
    if x.islower():
        lower = lower + 1
    elif x.isupper():
        upper = upper + 1
    elif x.isnumeric():
        num = num + 1
    else:
        cht = cht + 1
print('\n Total no. of lower case characters = ', lower,
      '\n Total no. of upper case characters = ', upper,
      '\n Total no. of numerical characters = ', num,
      '\n Total no. of special symbols = ', cht)
