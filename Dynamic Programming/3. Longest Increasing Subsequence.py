# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest
# subsequence of a given sequence such that all elements of the subsequence are sorted in
# increasing order.

ln = int(input())
arr = list(map(int, input().split()))
lis = [1]*ln
for x in range(0, ln):
    for y in range(0, x):
        if arr[x] > arr[y]:
            lis[x] = max(lis[x], lis[y] + 1)
print(max(lis))
