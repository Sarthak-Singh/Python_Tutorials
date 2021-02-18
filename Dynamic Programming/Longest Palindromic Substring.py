# Given a string S, find the longest palindromic substring in S. Substring of string
# S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads
# the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict,
# return the substring which occurs first ( with the least starting index ).
#
# NOTE: Required Time Complexity O(n2).
#
# Input:
# The first line of input consists number of the testcases. The following T lines consist
# of a string each.
#
# Output:
# In each separate line print the longest palindrome of the string given in the respective test case.

a = int(input())
for _ in range(a):
    s = list(input())
    n = len(s)
    t = [[0 for x in range(n)] for y in range(n)]
    max_len = 1
    for i in range(n):
        t[i][i] = 1
    st = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            t[i][i+1] = 1
            st = i
            max_len = 2
    for i in range(3, n+1):
        for x in range(n-i+1):
            y = x + i - 1
            if s[x] == s[y] and t[x+1][y-1] == 1:
                t[x][y] = 1
                if i > max_len:
                    st = x
                    max_len = i
    print(''.join(s[st: st + max_len]))
