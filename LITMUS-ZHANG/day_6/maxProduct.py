def maxProduct( nums) -> int:
    res = max(nums)
    curMin,curMax = 1, 1
    for n in nums:
        if n == 0 :
            curMin,curMax = 1, 1
            continue
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(n * curMax, n * curMin, n)
        res = max(res, curMax, curMin)
    return res

num = [-4,-3,-2]
print(maxProduct(num))