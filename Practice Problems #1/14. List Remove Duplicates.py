def duplicates_remover(x):
    m = []
    for y in x:
        if y in m:
            pass
        else:
            m.append(y)
    print(m)


duplicates_remover([5, 5, 5, 10, 15, 20, 25])

print('extras.................\n')

p = [5, 5, 5, 10, 15, 20, 25]
p = set(p)
p = list(p)
print(p)
