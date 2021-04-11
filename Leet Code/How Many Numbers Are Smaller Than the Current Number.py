def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    sm = [0]*len(nums)
    for x in range(len(nums)):
        if x != 0 and nums[x] == nums[x-1]:
            sm[x] = sm[x-1]
        else:
            sm[x] = sorted_nums.index(nums[x])
    return sm


print(smallerNumbersThanCurrent([8,0,8,8]))
