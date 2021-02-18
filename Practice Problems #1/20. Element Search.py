def element_checker(lst, x):
    if x in lst:
        return True
    else:
        return False


array = list(input("Enter the ordered list :\n"))
num = input('Enter the number to be searched :\n')
res = element_checker(array, num)
if res is True:
    print("The function returned : " + str(res))
    print("The number is there in the list.")
elif res is False:
    print("The function returned : " + str(res))
    print("The number is NOT in the list.")
