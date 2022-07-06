def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = {}
        
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset[nums[i]] = i
            print(hashset)
        
        return False
print(containsDuplicate([3,3]))