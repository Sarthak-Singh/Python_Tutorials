def maxDepth(s):
    max_d = 0
    count = 0
    for x in s:
        if x == '(':
            count += 1
            if count > max_d:
                max_d = count
        elif x == ')':
            count -= 1
    return max_d


print(maxDepth('(1+(2*3)+((8)/4))+1'))
