def fibonacci_series_gen(x):
    n = []
    n.append(1)
    n.append(1)
    y = 2
    while y < x:
        n.append(n[y-1]+n[y-2])
        y = y + 1
    print(n)


num = int(input("Enter the number of numbers in the sequence required : \n"))
fibonacci_series_gen(num)
