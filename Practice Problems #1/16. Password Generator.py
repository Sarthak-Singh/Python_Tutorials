import random


def pass_gen(x):
    y = 0
    n = []
    numbs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sml_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cap_alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbs = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+',
             '=', ':', ';', '<', '>', ',', '.', '?', '/', '|', '"']
    while y < x:
        n.append(random.randint(0, 88))
        if -1 < n[y] < 10:
            n[y] = numbs[n[y]]
        elif 9 < n[y] < 37:
            n[y] = sml_alph[n[y]-10]
        elif 36 < n[y] < 64:
            n[y] = cap_alph[n[y]-37]
        elif 63 < n[y] < 89:
            n[y] = symbs[n[y]-64]
        y = y + 1
    pass_word = ''.join(n)
    print(pass_word)


length = int(input('Enter the length of password required :\n'))
pass_gen(length)
