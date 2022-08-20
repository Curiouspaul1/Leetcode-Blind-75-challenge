class Solution:
    def canAttendMeetings(self, intervals):       
        if len(intervals) < 2:
            return True
        
        intervals.sort()

        prev_meeting_end = intervals [0][1]
        
        for meeting in intervals[1:]:
            if meeting[0] < prev_meeting_end:
                return False
  
            prev_meeting_end = meeting[1]
            
        return True
        
