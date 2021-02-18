# You are given a set of N types of rectangular 3-D boxes, where the ith box has
# height h, width w and length l. You task is to create a stack of boxes which is
# as tall as possible, but you can only stack a box on top of another box if the
# dimensions of the 2-D base of the lower box are each strictly larger than those
# of the 2-D base of the higher box. Of course, you can rotate a box so that any
# side functions as its base.It is also allowable to use multiple instances of the
# same type of box. You task is to complete the function maxHeight which returns
# the height of the highest possible stack so formed.
#
# Input:
# The first line of input contains an integer T denoting the number of test
# cases then T test cases follow. Each test case contains an integer N denoting
# the total no of boxes available. In the next line are 3*N space separated values
# denoting the height, width and length of the N boxes.
#
# Output:
# For each test case in a new line output will be the highest possible stack height
# which could be formed.

a = int(input())
for _ in range(a):
    n = int(input())*3
    a = list(map(int, input().split()))             # h, w, l
    ar = []
    for x in range(0, n-2, 3):
        ar.append([a[x], min(a[x + 1], a[x + 2]), max(a[x + 1], a[x + 2])])
        ar.append([a[x + 2], min(a[x], a[x + 1]), max(a[x], a[x + 1])])
        ar.append([a[x + 1], min(a[x + 2], a[x]), max(a[x + 2], a[x])])
    n_ar = sorted(ar, key=lambda d: (d[1]*d[2]), reverse=True)
    msh = [0]*n
    for x in range(n):
        msh[x] = n_ar[x][0]
    for i in range(1, n):
        for j in range(i):
            if n_ar[i][1] < n_ar[j][1] and n_ar[i][2] < n_ar[j][2]:
                if msh[i] < msh[j] + n_ar[i][0]:
                    msh[i] = msh[j] + n_ar[i][0]
    print(max(msh))
