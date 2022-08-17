class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]: 
            i += 1 
            

        preNonIntersectingCount = i
        
        minS, maxE = newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]: 
            minS, maxE, i = min(minS, intervals[i][0]), max(maxE, intervals[i][1]), i+1
      
        return intervals[:preNonIntersectingCount] + [[minS, maxE]] + intervals[i:]
