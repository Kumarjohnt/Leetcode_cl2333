class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        
        if num == 1:
            return [0, 1]
        
        res = [0, 1]
        for i in range(2, num + 1):
            now = i & 1
            prev = i >> 1
            res.append(now + res[prev])
            
        return res