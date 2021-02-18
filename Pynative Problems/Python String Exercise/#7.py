def equality_checker(a, b):
    x = list(a)
    y = list(b)
    for p in x:
        if p in y:
            continue
        else:
            return False
    return True


wrd1 = input('Enter characters to check for:\n')
wrd2 = input('Enter the word:\n')
print(equality_checker(wrd1, wrd2))
