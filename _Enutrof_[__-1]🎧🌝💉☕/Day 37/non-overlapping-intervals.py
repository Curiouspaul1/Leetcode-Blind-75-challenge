class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = -1
        count = 0
        for i, interval in enumerate(intervals):
            if i > 0:
                if interval[0] >= end:
                    end = interval[1]
                else:
                    count += 1
                    end = min(end, interval[1])
            else:
                end = interval[1]
        return count
