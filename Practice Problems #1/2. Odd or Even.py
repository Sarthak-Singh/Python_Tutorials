print("Enter a number :")
num = input()
rem2 = int(num) % 2
rem4 = int(num) % 4
if rem2 is 1:
    print(num + " is an odd number.")

elif rem2 is 0:
    if rem4 is 0:
        print(num + " is a multiple of 4.")
    else:
        print(num + " is an even number.")

print("Second Extras..............")
print("\n")
print("Enter the dividend :")
num = input()
print("Enter the divisor :")
check = input()
result = int(num) % int(check)
if int(result) is 0:
    print(check + " is a multiple of " + num)
else:
    print(check + " can't properly divide " + num)
