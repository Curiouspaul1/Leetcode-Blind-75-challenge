class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        result = []
        for i in range(len(intervals)):
            if not result:
                result.append(intervals[i])
            else:
                if result[-1][1] >= intervals[i][0]:
                    result[-1][1] = max(result[-1][1], intervals[i][1])
                else:
                    result.append(intervals[i])
        return result
            
