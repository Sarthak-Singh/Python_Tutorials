def subtractProductAndSum(n):
    numbers = [int(num) for num in str(n)]
    num_sum = 0
    product = 1
    for num in numbers:
        product = product * num
        num_sum += num
    return product - num_sum


print(subtractProductAndSum(4421))
