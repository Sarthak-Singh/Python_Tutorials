def reverse_check(number):
    original_num = number
    reverse_num = 0
    while number > 0:
        remainder = number % 10
        reverse_num = (reverse_num * 10) + remainder
        number = number // 10
    if original_num == reverse_num:
        return True
    else:
        return False


print("original and revers number is equal")
print(reverse_check(1221))
