from collections import Counter
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        heap = []
        for num, freq in counter.items():
            heappush(heap, (-freq, num))
        
        result = []
        while k > 0 and heap:
            freq, num = heappop(heap)
            result.append(num)
            k -= 1
        
        return result