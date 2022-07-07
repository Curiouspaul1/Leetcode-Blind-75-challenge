def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))


# print(containsDuplicate([1,2,3,4,5,6,7,8,9,10]))
# print(containsDuplicate([1,2,3,4,5,6,7,8,9,10,1]))
# print(containsDuplicate([1,2,3,1]))

nums = [1,2,3,4, 1]
a = set(nums)
print(a, len(a), len(nums))