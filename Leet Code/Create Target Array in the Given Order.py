def createTargetArray(nums, index):
    tar_arr = []
    for x in range(len(index)):
        tar_arr.insert(index[x], nums[x])
    return tar_arr


print(createTargetArray([1,2,3,4,0], [0,1,2,3,0]))
