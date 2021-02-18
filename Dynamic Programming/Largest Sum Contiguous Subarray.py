# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# The description of T test cases follows. The first line of each test case contains
# a single integer N denoting the size of array. The second line contains N
# space-separated integers A1, A2, ..., AN denoting the elements of the array.
#
# Output:
# Print the maximum sum of the contiguous sub-array in a separate line for each test case.

a = int(input())
for _ in range(a):
    n = int(input())
    a = list(map(int, input().split()))
    curr_max = a[0]
    max_so_far = a[0]
    for x in range(1, n):
        curr_max = max(a[x], curr_max + a[x])
        max_so_far = max(max_so_far, curr_max)
    print(max_so_far)
