s = input("Enter the word:\n")
num = len(s)
ind = list(s)
n = 0
while n <= num:
    if n % 2 == 0:
        print(ind[n])
    n = n + 1
