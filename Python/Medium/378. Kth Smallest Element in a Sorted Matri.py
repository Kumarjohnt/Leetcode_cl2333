from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m,n = len(matrix), len(matrix[0])
        heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            val, i, j = heappop(heap)
            k -= 1
            
            if i + 1 < m and (matrix[i + 1][j], i + 1, j) not in heap:
                heappush(heap, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and (matrix[i][j + 1], i, j + 1) not in heap:
                heappush(heap, (matrix[i][j + 1], i, j + 1))
                
        return val
            