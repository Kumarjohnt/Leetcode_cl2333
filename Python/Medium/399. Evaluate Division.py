from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (x,y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1/v
        
        def bfs(start, end):
            if not (start in graph and end in graph):
                return -1.0
            from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (x,y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1/v
        
        def bfs(start, end):
            if not (start in graph and end in graph):
                return -1.0
            
            q, seen = deque([(start, 1.0)]), set()
            while q:
                x, ratio = q.popleft()
                
                if x == end:
                    return ratio
                seen.add(x)
                for y in graph[x]:
                    if y not in seen:
                        q.append((y, ratio*graph[x][y]))
            
            return -1.0
        
        
        return [bfs(x, y) for (x, y) in queries]
            q, seen = deque([(start, 1.0)]), set()
            while q:
                x, ratio = q.popleft()
                
                if x == end:
                    return ratio
                seen.add(x)
                for y in graph[x]:
                    if y not in seen:
                        q.append((y, ratio*graph[x][y]))
            
            return -1.0
        
        
        return [bfs(x, y) for (x, y) in queries]