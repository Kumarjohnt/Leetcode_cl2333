directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        is_island = disjoint_set()
        for p in map(tuple, positions):
            is_island.add(p)
            for (x,y) in directions:
                q = (p[0] + x, p[1] + y)
                if q in is_island.parent:
                    is_island.union(p, q)
            ans.append(is_island.count)
            
        return ans
        
        
class disjoint_set:
    def __init__(self):
        self.rank = {}
        self.size = {}
        self.count = 0
        self.parent = {}
    
    def add(self, x):
        if x in self.parent:
            return
        self.rank[x] = 1
        self.size[x] = 1
        self.parent[x] = x
        self.count += 1
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
        self.count -= 1