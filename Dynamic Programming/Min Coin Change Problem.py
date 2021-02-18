# Given a value V. You have to make change for V cents, given that you have infinite
# supply of each of C{ C1, C2, .. , Cm} valued coins. Find the minimum number of coins
# to make the change.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is V and N, V is the value of cents and N is the
# number of coins. The second line of each test case contains N input C[i], value of
# available coins.
#
# Output:
# Print the minimum number of coins to make the change, if not possible print "-1".

a = int(input())
for _ in range(a):
    v = int(input().split()[0])
    c = sorted(list(map(int, input().split())))
    n = len(c)
    tb = [0 for x in range(v+1)]
    tb[0] = 0
    for a in range(1, v+1):
        tb[a] = 10**6
    for i in range(1, v+1):
        for j in range(n):
            if c[j] <= i:
                tb[i] = min(tb[i], tb[i-c[j]] + 1)
    if tb[v] != 10**6:
        print(tb[v])
    else:
        print(-1)
