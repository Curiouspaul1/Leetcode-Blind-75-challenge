from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x[0])
        
        free_rooms = []
        heappush(free_rooms, intervals[0][1])
        
        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heappop(free_rooms)
            
            heappush(free_rooms, interval[1])
        
        return len(free_rooms)
