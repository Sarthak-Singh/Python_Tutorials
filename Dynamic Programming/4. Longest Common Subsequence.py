# Given two sequences, find the length of longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not
# necessarily contiguous.
#
# Input:
# First line of the input contains no of test cases  T,the T test cases follow.
# Each test case consist of 2 space separated integers A and B denoting the size of string
# str1 and str2 respectively
# The next two lines contains the 2 string str1 and str2 .
#
# Output:
# For each test case print the length of longest  common subsequence of the two strings .

a = int(input())
for x in range(a):
    s = list(map(int, input().split()))
    w1 = input()
    w2 = input()
    com = [[0]*(s[1]+1) for i in range(s[0]+1)]
    for y in range(s[0] + 1):
        for z in range(s[1] + 1):
            if y == 0 or z == 0:
                com[y][z] = 0
            elif w1[y-1] == w2[z-1]:
                com[y][z] = com[y-1][z-1] + 1
            else:
                com[y][z] = max(com[y-1][z], com[y][z-1])
    print(com[s[0]][s[1]])
