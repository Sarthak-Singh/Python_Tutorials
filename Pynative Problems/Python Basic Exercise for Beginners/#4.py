wrd = input('Enter a word:\n')
s = int(input('Enter breakpoint:\n'))
dict = list(wrd)
new_wrd = ''
while s <= len(wrd)-1:
    new_wrd = new_wrd + dict[s]
    s = s + 1
print(new_wrd)
