from heapq import *
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        
        heap = []
        for c, freq in counter.items():
            heappush(heap, (-freq, c))
        
        k, res = n + 1, 0
        waitlist = []
        while heap:
            while k > 0 and heap:
                freq, c = heappop(heap)
                freq  += 1
                res += 1
                k -= 1
                if freq < 0:
                    waitlist.append((freq, c))
            
            if waitlist:
                res += k
            while waitlist:
                (freq, c) = waitlist.pop()
                heappush(heap, (freq, c))
            k = n + 1
        
        return res
                    
                
                
            