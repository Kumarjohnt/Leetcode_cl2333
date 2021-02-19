"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        schedule = sorted([i for s in schedule for i in s], key = lambda x: x.start)
        result, pre = [], schedule[0]
        for i in schedule[1:]:
            if i.start > pre.end:
                result.append(Interval(pre.end, i.start))
                pre.end = i.end
            else:
                pre.end = max(i.end, pre.end)
        return result
            
        
        
        