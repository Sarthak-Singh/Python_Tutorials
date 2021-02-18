f1 = open(r"Input Files\Prime No.s Between 1-1000.txt", 'r')
prime = f1.read().split()
f1.close()

f2 = open(r"Input Files\Happy No.s Between 1-1000.txt", 'r')
happy = f2.read().split()
f2.close()

common = []
for x in prime:
    if x in happy:
        common.append(x)
    else:
        pass
print(common)
