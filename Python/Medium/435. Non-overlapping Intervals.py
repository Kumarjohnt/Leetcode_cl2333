class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x : (x[0], x[1]))
        count, prev = 0, intervals[0]
        
        for i in intervals[1:]:
            if i[0] < prev[1]:
                count += 1  
                if i[1] < prev[1]:
                    prev[1] = i[1]
            else:
                prev[1] = i[1]
                
            
        
        return count