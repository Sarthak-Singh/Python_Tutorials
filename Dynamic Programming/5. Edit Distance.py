# Given two strings str1 and str2 and below operations that can performed on str1.
# Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
#
# Insert
# Remove
# Replace
# All of the above operations are of equal cost.

a = list(input())
b = list(input())
ed = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for x in range(len(a)+1):
    for y in range(len(b)+1):
        if x == 0:
            ed[x][y] = y
        elif y == 0:
            ed[x][y] = x
        elif a[x-1] == b[y-1]:
            ed[x][y] = ed[x-1][y-1]
        else:
            ed[x][y] = 1 + min(ed[x-1][y-1], ed[x-1][y], ed[x][y-1])
print(ed[len(a)][len(b)])
