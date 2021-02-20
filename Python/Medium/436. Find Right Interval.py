class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = []
        data = sorted((inter[0], i) for i,inter in enumerate(intervals))
        for i in intervals:
            index = bisect.bisect_left(data, (i[1],))
            if index >= len(intervals):
                result.append(-1)
            else:
                result.append(data[index][1])
        return result
            