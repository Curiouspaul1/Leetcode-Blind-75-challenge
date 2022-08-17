class Solution(object):
    def insert(self, intervals, newInterval):
        output = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                newInterval =[min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1])]
                
        output.append(newInterval)
        return output
