# Given an array A of N positive integers. Find the sum of maximum sum increasing subsequence
# of the given array.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. The first
# line of each test case is N(the size of array). The second line of each test case contains
# array elements.
#
# Output:
# For each test case print the required answer in new line.

t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    msis = [ar[x] for x in range(n)]
    for i in range(1, n):
        for j in range(i):
            if ar[i] > ar[j] and msis[i] < msis[j] + ar[i]:
                msis[i] = msis[j] + ar[i]
    print(max(msis))
