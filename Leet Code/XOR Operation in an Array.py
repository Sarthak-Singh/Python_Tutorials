def xorOperation(n, start):
    ans = start
    for x in range(1, n):
        ans ^= (start + 2*x)
    return ans


print(xorOperation(10, 5))
