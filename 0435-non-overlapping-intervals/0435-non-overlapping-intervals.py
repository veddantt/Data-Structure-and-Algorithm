class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])

        count=1
        end_time=intervals[0][1]
        for i in range(1,len(intervals)):
            start_time,curr_end_time=intervals[i]
            
            if start_time>=end_time:
                count+=1
                end_time=curr_end_time
        
        return len(intervals)-count