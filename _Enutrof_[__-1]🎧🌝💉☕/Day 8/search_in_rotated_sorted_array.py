class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        start = 0
        stop = self.length
        while start < stop:
            mid = (start + stop) // 2
            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                stop = mid
                
        return start
    def binSearch(self, nums: List[int], target: int) -> int:
        start = 0
        stop = self.length
        while start < stop:
            mid = (start + stop) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                stop = mid
    
    def search(self, nums: List[int], target: int) -> int:
        self.length = len(nums)
        minimum = self.findMinIndex(nums)
        print(minimum)
        searched = self.binSearch(nums[minimum:] + nums[:minimum], target)
        print(searched)
        if searched is not None:
            deviation = self.length - minimum
            index = searched - deviation
            return index if index >= 0 else index + self.length
        else:
            return -1
    
