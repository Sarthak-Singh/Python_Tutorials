# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack. In other words, given two integer
# arrays v[0..n-1] and wt[0..n-1] which represent values and weights associated with
# n items respectively. Also given an integer W which represents knapsack capacity,
# find out the maximum value subset of v[] such that sum of the weights of this subset
# is smaller than or equal to W. You cannot break an item, either pick the complete item,
# or don’t pick it (0-1 property).

a = int(input())
for _ in range(a):
    n = int(input())
    W = int(input())
    v = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    K = [[0 for x in range(W+1)] for y in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(v[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(K[n][W])
