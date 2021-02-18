fw = open(r'Input Files\names.txt', 'r')
names = fw.read()
fw.close()

array = names.split()

counter = {}
y = 0
for x in array:
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

print(counter)
