
# Approach 1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current = 0
        for i in range(len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            maxSum = max(current, maxSum)
        return maxSum
                
# Approach 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum_so_far = nums[0]
        curr = nums[0]
        
        for i in range(1,len(nums)):
            curr = max(nums[i], curr+nums[i])
            maximum_sum_so_far = max(maximum_sum_so_far, curr)
        
        return maximum_sum_so_far

# Approach 3
class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
    m1=arr[0]
    m2=0
    for i in range(len(arr)):
        m2=m2+arr[i]
        if m2<0:
            m2=0
        elif m1<m2:
            m1=m2
    if m1<0:
        return 0
    return m1


# Approach 4
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _, _, _, m = self.daq(nums)
        return m
    
    def daq(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]] * 4

        mid = len(nums) // 2
        a1, l1, r1, m1 = self.daq(nums[mid:])
        a2, l2, r2, m2 = self.daq(nums[:mid])

        a = a1 + a2                                 # complete sum over nums
        l = max(l1, a1, a1 + l2, a)                 # largest sum starting with nums[0]
        r = max(r2, a2, a2 + r1, a)                 # largest sum ending with nums[-1]
        m = max(m1, m2, r1 + l2, a, l, r)           # largest sum for arbitrary subarray
        return a, l, r, m



#ApproCH 5
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(1,len(nums)):
                nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)
