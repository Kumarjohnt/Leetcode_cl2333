class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        l1, l2 = len(words1), len(words2)
        if l1 != l2:
            return False
        
        parent = {}
        def find(a):
            if a not in parent:
                parent[a] = a
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]
        
        for a, b in pairs:
            x, y = find(a), find(b)
            parent[x] = y
        
        for i in range(l1):
            a, b = find(words1[i]), find(words2[i])
            if a != b:
                return False
        
        return True
            
        