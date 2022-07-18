
def missingNumber( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # First Approach
        # loop through the array in the range (0,n)
        # check for each element if it exist in the array if not return the number
        a = len(nums)
        for i in range(a+1):
            if i in nums:
                pass
            else:
                return i