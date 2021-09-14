def decompressRLElist(nums):
    ans = []
    for x in range(len(nums)):
        if x % 2 == 0:
            ans.extend([nums[x+1]]*nums[x])
    return ans


print(decompressRLElist([1,2,3,4]))
