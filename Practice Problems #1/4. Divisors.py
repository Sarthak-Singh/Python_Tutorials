num = int(input("Enter the number :\n"))
x = 1
print("The Divisors are :")
while x < num + 1:
    if num % x is 0:
        print(x)
    x = x + 1
