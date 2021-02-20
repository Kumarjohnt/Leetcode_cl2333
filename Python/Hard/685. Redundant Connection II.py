class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        parent = list(range(len(edges)))
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
    
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            parent[y] = x
            return True
        
        can1, can2, to_node = None, None, {}
        for (x, y) in edges:
            if y in to_node:
                can1, can2 = to_node[y], (x,y)
                break
            to_node[y] = [x, y]
        
        for (x,y) in edges:
            if (x,y) == can2:
                continue
            if not union(x - 1, y - 1):
                if can1:
                    return can1
                return (x, y)
            
        return can2
        