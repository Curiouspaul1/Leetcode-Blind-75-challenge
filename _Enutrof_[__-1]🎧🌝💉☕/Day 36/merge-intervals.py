class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        i = 0
        
        while  i < len(intervals):
            start, stop = intervals[i]
            end = i
            
            while end + 1 < len(intervals):
                if start <= intervals[end+1][0] <= stop:
                    start = min(intervals[end+1][0], start)
                    stop = max(intervals[end+1][1], stop)
                    end += 1
                else:
                    break
                    
            intervals[i:end+1] = [[start, stop]]
            i += 1
        
        return intervals
      
