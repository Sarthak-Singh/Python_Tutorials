def kidsWithCandies(candies, extraCandies):
    maxC = max(candies)
    check = [False]*len(candies)
    for x in range(len(candies)):
        if candies[x] + extraCandies >= maxC:
            check[x] = True
    return check


print(kidsWithCandies([12, 1, 12], 10))
