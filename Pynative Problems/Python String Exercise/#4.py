word = input('Enter a word:\n')
lower = []
upper = []
n_word = ''
for x in word:
    if x.islower():
        lower.append(x)
    else:
        upper.append(x)
y = n_word.join(lower+upper)
print(y)
