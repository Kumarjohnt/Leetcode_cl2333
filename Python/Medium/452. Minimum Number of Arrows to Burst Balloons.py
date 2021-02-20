class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[0])
        count = 1
        prev = points[0]
        for point in points[1:]:
            if point[0] > prev[1]:
                count += 1
                prev = point
            else:
                prev[0] = max(point[0], prev[0])
                prev[1] = min(point[1], prev[1])
        
        return count
                    