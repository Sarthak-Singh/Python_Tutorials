# Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number
# of distinct combinations to reach the given score.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases follow.
# The first line of each test case is n.
#
# Output:
# For each testcase, in a new line, print number of ways/combinations to reach the given score.

t = int(input())
for _ in range(t):
    s = int(input())
    w = [0 for x in range(s+1)]
    w[0] = 1
    for y in range(3, (s+1)):
        w[y] += w[y-3]
    for y in range(5, (s+1)):
        w[y] += w[y-5]
    for y in range(10, (s+1)):
        w[y] += w[y-10]
    print(w[s])
