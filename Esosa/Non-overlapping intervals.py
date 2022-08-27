class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        res= 0
        previous= intervals[0][1]
        for start, end in intervals[1:]:
            if start >= previous:
                previous= end
            else:
                res +=1
                previous = min(end, previous)
        return res
