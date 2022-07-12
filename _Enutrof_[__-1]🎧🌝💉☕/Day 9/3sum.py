class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        seen = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] in seen:
                continue
            seen.add(nums[i])
            target = -nums[i]
            start = i + 1
            end = len(nums) - 1
    
            while start < end:
                current_sum = nums[start] + nums[end]
                if current_sum < target:
                    start += 1
                elif current_sum > target:
                    end -= 1
                else:
                    triplet = [nums[i], nums[start], nums[end]]
                    output.append(triplet)
    
                    while start < end and nums[start] == triplet[1]:
                        start += 1

                    while start < end and nums[end] == triplet[2]:
                        end -= 1
    
        return output
