def runningSum(list):
    sum_list = [0] * len(list)
    sum = 0
    for x in range(len(list)):
        sum += list[x]
        sum_list[x] = sum
    return sum_list


print(runningSum([2, 3, 6, 7]))
