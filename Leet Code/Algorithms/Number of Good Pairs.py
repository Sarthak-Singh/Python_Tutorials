def numIdenticalPairs(nums):
    pairs = 0
    for num in set(nums):
        dup = nums.count(num)
        pairs += dup * (dup - 1) // 2
    return pairs
