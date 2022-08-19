class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        removed = 0
        prev_end = intervals[0][1]
        
        for interval in intervals[1:]:
            if interval[0] >= prev_end:
                prev_end = interval[1]
            else:
                removed += 1
                prev_end = min(prev_end, interval[1])
        return removed
