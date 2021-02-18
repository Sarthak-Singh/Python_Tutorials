l1 = [10, 20, 23, 11, 17]
l2 = [13, 43, 24, 36, 12]
l3 = []
for x in l1:
    if x % 2 != 0:
        l3.append(x)
for y in l2:
    if y % 2 == 0:
        l3.append(y)
print(l3)
