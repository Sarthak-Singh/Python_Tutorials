def numJewelsInStones(jewels, stones):
    total = 0
    for x in jewels:
        total += stones.count(x)
    return total
