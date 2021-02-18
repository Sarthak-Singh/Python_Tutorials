# Given a positive integer N, count all possible distinct binary strings of length N such that
# there are no consecutive 1’s. Output your answer mod 10^9 + 7.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. The description
# of T test cases follows.
# Each test case contain an integer N representing length of the binary string.
#
# Output:
# Print the count number of binary strings without consecutive 1’s of length N.

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0 for x in range(n)]
    b = [0 for y in range(n)]
    a[0] = b[0] = 1
    for i in range(1, n):
        a[i] = a[i-1] + b[i-1]
        b[i] = a[i-1]
    print(a[n-1] + b[n-1])
