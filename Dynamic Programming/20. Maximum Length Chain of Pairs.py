# You are given n pairs of numbers. In every pair, the first number is always smaller
# than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain
# of pairs can be formed in this fashion. Find the longest chain which can be formed
# from a given set of pairs.

a = int(input())
for _ in range(a):
    n = int(input())
    b = list(map(int, input().split()))
    ar = []
    for x in range(0, n*2-1, 2):
        ar.append([b[x], b[x+1]])
    n_ar = sorted(ar)                           # Sorted i/p Array
    mcl = [1 for p in range(n)]
    for x in range(1, n):
        for y in range(x):
            if n_ar[x][0] > n_ar[y][1] and mcl[x] < mcl[y] + 1:
                mcl[x] = mcl[y] + 1
    print(max(mcl))
