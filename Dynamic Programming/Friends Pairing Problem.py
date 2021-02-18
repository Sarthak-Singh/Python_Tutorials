# Given n friends, each one can remain single or can be paired up with some other friend.
# Each friend can be paired only once. Find out the total number of ways in which friends
# can remain single or can be paired up.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T
# test cases follow. Each test case contains an integer N.
#
# Output:
# For each test case in a new line print the required answer mod 10^9+7.

t = int(input())
for _ in range(t):
    n = int(input())
    p = [0 for x in range(n+1)]
    for i in range(n+1):
        if i <= 2:
            p[i] = i
        else:
            p[i] = p[i-1] + (i-1)*p[i-2]
    print(p[n] % (10**9+7))
