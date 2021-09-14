def balancedStringSplit(s):
    count = pairs = 0
    for x in s:
        if x == 'L':
            count += 1
        else:
            count -= 1
        if count == 0:
            pairs += 1
    return pairs


print(balancedStringSplit("RLRRRLLRLL"))
