# Given an array of positive integers. The task is to print the maximum length of
# Bitonic subsequence.
# a subsequence of array is called Bitonic if it is first increasing, then decreasing.
#
# Input:
# First line contains T test cases. First line of every test case consists of N ,
# denoting number of elements in an array. Second line of every test consists of
# elements in array.
#
# Output:
# For each testcase, in a new line, print the length of longest bitonic sequence.

a = int(input())
for _ in range(a):
    n = int(input())
    ar = list(map(int, input().split()))
    lis = [1 for x in range(n)]              # Longest Increasing Subsequence
    for i in range(1, n):
        for j in range(i):
            if ar[i] > ar[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    lds = [1 for x in range(n)]              # Longest Decreasing Subsequence
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if ar[i] > ar[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    max_seq = lis[0] + lds[0] - 1            # Longest Bitonic Subsequence
    for m in range(n):
        max_seq = max(lis[m] + lds[m] - 1, max_seq)
    print(max_seq)
