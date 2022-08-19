from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        overlapping_interval_count = 0
        
        prevEnd= intervals[0][1]

        for i in intervals[1:]:
            if i[0] >= prevEnd:
                prevEnd = i[1]
            else:
                overlapping_interval_count +=1
                prevEnd = min(i[1], prevEnd)
                
                
        return overlapping_interval_count
                