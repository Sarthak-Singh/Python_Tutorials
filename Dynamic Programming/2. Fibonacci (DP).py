n = int(input())
fib = [1]*n
for x in range(2, n):
    fib[x] = fib[x-1] + fib[x-2]
print(fib[n-1])
