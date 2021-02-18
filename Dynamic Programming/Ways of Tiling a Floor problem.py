# Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1, the task is to find the
# number of ways the floor can be tiled. A tile can either be placed horizontally i.e as a
# 1 x 2 tile or vertically i.e as 2 x 1 tile.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. The first
# line of each test case is W.
#
# Output:
# Print number of ways the floor can be tiled in a separate line.

a = int(input())
for _ in range(a):
    w = int(input())
    c = [0 for x in range(w+1)]
    c[1] = 1
    c[2] = 2
    for y in range(3, w+1):
        c[y] = c[y-1] + c[y-2]
    print(c[w])
