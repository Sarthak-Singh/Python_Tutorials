# Suppose you have N eggs and you want to determine from which floor in a K-floor building you
# can drop an egg such that it doesn't break. You have to determine the minimum number of
# attempts you need in order find the critical floor in the worst case while using the best
# strategy.There are few rules given below.
#
# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The effect of a fall is the same for all eggs.
# If the egg doesn't break at a certain floor, it will not break at any floor below.
# If the eggs breaks at a certain floor, it will break at any floor above.
#
# Input:
# The first line of input is  T denoting the number of testcases.Then each of the T lines contains
# two positive integer N and K where 'N' is the number of eggs and 'K' is number of floor in
# building.
#
# Output:
# For each test case, print a single line containing one integer the minimum number of attempt
# you need in order find the critical floor.

a = int(input())
for _ in range(a):
    e_f = list(map(int, input().split()))
    e = e_f[0]
    f = e_f[1]
    K = [[0 for x in range(f+1)] for y in range(e+1)]
    for i in range(1, e + 1):
        K[i][1] = 1
    for j in range(1, f + 1):
        K[1][j] = j
    for i in range(2, e+1):
        for j in range(2, f+1):
            K[i][j] = 999999
            for x in range(1, j+1):
                K[i][j] = min(1 + max(K[i-1][x-1], K[i][j-x]), K[i][j])
    print(K[e][f])
