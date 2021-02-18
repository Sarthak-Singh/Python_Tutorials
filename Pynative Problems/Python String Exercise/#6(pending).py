wrd1 = input('Enter the first word:\n')
wrd2 = input('Enter the second word:\n')
n_wrd = ''
a = 0
b = len(wrd2)
while a <= len(wrd1)-1 or b >= 0:
    n_wrd = n_wrd + wrd1[a]
    n_wrd = n_wrd + wrd2[b-1]
    if a != len(wrd1):  # using or in the loop creates an error,
        a = a + 1       # because if a or b reaches termination, it is yet run in the loop
    if b != 0:          # and hence its value is changed and the index get out of range.
        b = b - 1
print(a, b)
if a != len(wrd1):
    n_wrd = n_wrd + wrd1[a:]
elif b != 0:
    n_wrd = n_wrd + wrd2[:b]
print(n_wrd)
