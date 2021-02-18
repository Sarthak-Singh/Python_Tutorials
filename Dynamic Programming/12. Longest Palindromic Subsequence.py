# Given a String, find the longest palindromic subsequence
#
# Input:
# The first line of input contains an integer T, denoting no of test cases.
# The only line of each test case consists of a string S(only lowercase)
#
# Output:
# Print the Maximum length possible for palindromic subsequence.

a = int(input())
for _ in range(a):
    s = list(input())
    lps = [[0 for x in range(len(s))] for y in range(len(s))]
    for i in range(len(s)):
        lps[i][i] = 1
    for x in range(2, len(s)+1):
        for y in range(len(s) - x + 1):
            z = y + x - 1
            if s[y] == s[z] and x == 2:
                lps[y][z] = 2
            elif s[y] == s[z]:
                lps[y][z] = lps[y+1][z-1] + 2
            else:
                lps[y][z] = max(lps[y][z-1], lps[y+1][z])
    print(lps[0][len(s)-1])
