class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx1, idx2 = 0, 0
        result = []
        
        while idx1 < len(firstList) and idx2 < len(secondList):
            start1, end1, start2, end2 = firstList[idx1][0], firstList[idx1][1], secondList[idx2][0], secondList[idx2][1]
            
            if max(start1, start2) <= min(end1, end2):
                result.append([max(start1, start2),  min(end1, end2)])
            
            if end1 < end2:
                idx1 += 1
            else:
                idx2 += 1
        
        return result