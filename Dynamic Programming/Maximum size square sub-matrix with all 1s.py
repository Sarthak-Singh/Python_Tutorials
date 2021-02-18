# Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
#
# Input:
#
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is n and m,n is the number of rows and m is the number of columns.
# The second line of each test case contains array C[n][m] in row major form.
#
# Output:
#
# Print maximum size square sub-matrix.

t = int(input())
for _ in range(t):
    n_m = list(map(int, input().split()))
    el = list(map(int, input().split()))
    ar = []
    for x in range(n_m[0]):
        ar.append(el[n_m[1]*x: n_m[1]*(x+1)])
    s = [[0 for x in range(n_m[1])] for y in range(n_m[0])]
    s[0] = ar[0]
    for x in range(n_m[0]):
        s[x][0] = ar[x][0]
    for x in range(1, n_m[0]):
        for y in range(1, n_m[1]):
            if ar[x][y] == 1:
                s[x][y] = min(s[x-1][y], s[x][y-1], s[x-1][y-1]) + 1
            else:
                s[x][y] = 0
    max = 0
    for x in s:
        for y in x:
            if y > max:
                max = y
    print(max)
