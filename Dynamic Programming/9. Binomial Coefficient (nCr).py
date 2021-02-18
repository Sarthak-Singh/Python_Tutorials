# Write a function that takes two parameters n and k and returns the value of Binomial
# Coefficient C(n, k).
# Find nCr for given n and r.
#
# Input:
# First line contains number of test cases T. T testcases follow. Each testcase contains 1
# line of input containing 2 integers n and r separated by a space.
#
# Output:
# For each testcase, in a new line, find the nCr. Modulus your output to 109+7.
#
# Standard formula: C(n, k) = C(n-1, k-1) + C(n-1, k)
#                   C(n, 0) = C(n, n) = 1

a = int(input())
for _ in range(a):
    n_r = list(map(int, input().split()))
    n = n_r[0]
    r = n_r[1]
    C = [[0 for x in range(r+1)] for y in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, r) + 1):
            if i == 0 or i == j:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    print(C[n][r])
