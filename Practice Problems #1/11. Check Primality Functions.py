num = int(input('Enter the number : \n'))

x = 2
res = int
while x < num:
    if num % x != 0:
        res = 1
    else:
        res = 0
        break
    x = x + 1
if res is 1:
    print("This is a prime number!")
elif res is 0:
    print("This is NOT a prime number!")
