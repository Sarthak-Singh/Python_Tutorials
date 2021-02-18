# Given a fence with n posts and k colors, find out the number of ways of painting the fence such
# that at most 2 adjacent posts have the same color. Since answer can be large return it modulo
# 10^9 + 7.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case
# contains two integers n and k.
#
# Output:
# Print an integer which denoted the number of ways in which the fence can be painted.(modulo 109 + 7)

a = int(input())
for _ in range(a):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    pw = [0]*(n+1)
    pw[1] = k
    d = k
    s = 0
    for i in range(2, n+1):
        s = d
        d = pw[i-1]*(k-1)
        pw[i] = s + d
    print(pw[n] % (10**9 + 7))
