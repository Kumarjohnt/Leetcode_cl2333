class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = list(range(len(edges)))
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
    
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            parent[x] = y
            return True
        
        for (x,y) in edges:
            if not union(x - 1, y - 1):
                return [x, y]
            