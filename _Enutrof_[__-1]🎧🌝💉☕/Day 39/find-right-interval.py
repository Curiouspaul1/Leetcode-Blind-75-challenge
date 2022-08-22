class Solution:
    def binarySearch(self, end):
        l, r = 0, len(self.store)-1
        res = -1
        while l <= r:
            mid = l+(r-l)//2
            if self.store[mid][0][0]>=end:
                res = self.store[mid][1]
                r = mid-1
            else:
                l = mid+1
        return res
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        self.store =sorted([[intervals,i] for i,intervals in enumerate(intervals)])
        res=[]
        for start, end in intervals:
            res.append(self.binarySearch(end))
        return res
      
