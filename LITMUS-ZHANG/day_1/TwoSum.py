def twoSum(nums , target):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums[i+1:]:
            return [i, nums[i+1:].index(diff) + i + 1]
        # if diff in nums:
        #     return [i, nums.index(diff)]


print(twoSum([2,7,11,15], 9))