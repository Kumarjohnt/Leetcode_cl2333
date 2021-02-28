class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        d = {}
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                d[i+j] = d.get(i+j, []) + [matrix[i][j]]
                
        result = []
        for i in sorted(d.keys()):
            if i % 2 == 0:
                result += d[i][::-1]
            else:
                result += d[i]
        
        return result