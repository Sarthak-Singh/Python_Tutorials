import random

fl = open(r'Input Files\Sowpods Dictionary.txt', 'r')
lst = fl.read()
fl.close()
dctn = lst.split()
k = random.randint(0, 267750)
print(dctn[k])
