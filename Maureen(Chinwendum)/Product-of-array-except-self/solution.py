class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[1]*len(nums)
        first=1
        for x in range(len(nums)):
            product[x]=first
            first=nums[x]*first
        print(product)
        rev_list_num=list(range(len(nums)))
        rev_list_num.reverse()
        print(rev_list_num)
        Post=1
        for x in rev_list_num:
            product[x]=Post * product[x]
            Post=nums[x]*Post
        return product
            
            
            
            
        