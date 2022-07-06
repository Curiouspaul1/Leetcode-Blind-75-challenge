def containsDuplicate(self, nums):
        if(len(nums)!= len(set(nums))): return True
        else: return False