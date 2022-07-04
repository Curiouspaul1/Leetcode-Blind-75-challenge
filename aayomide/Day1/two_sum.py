def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # create key value pairs, where k is remainder of the difference btw target and an element in the array and 
    # value is the index of the element in the array, this is since we need to return indices of matching elements
    
    dict_ = {}

    for i,n in enumerate(nums):
        remainder = target-n
        if n in dict_:
            num1, num2 = [dict_[n], i]
        else:
            dict_[remainder] = i
    return([num1, num2])
