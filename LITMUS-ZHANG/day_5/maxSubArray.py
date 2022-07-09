def maxSubArray(nums) -> int:
    left = nums[0]
    ArraySum = 0
    for n in nums:
        if ArraySum < 0:
            ArraySum = 0
        ArraySum += n
        left = max(left, ArraySum)
    return left
        # curSum = nums[: n]
        # if curSum > ArraySum:
        #     ArraySum = curSum
        #     left = nums[]
        
