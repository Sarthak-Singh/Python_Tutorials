a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("extra 1.............")
b = []
for x in a:
    if x < 5:
        b.append(x)

print(b)
print("\n")
print("extra 2.............")
c = []
print("Enter the Max. Limit :")
lim = input()
for y in a:
    if y < int(lim):
        c.append(y)

print(c)
