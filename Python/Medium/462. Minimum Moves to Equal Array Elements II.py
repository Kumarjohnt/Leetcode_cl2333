import math
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        median = sorted(nums)[n//2]
        
        result = 0
        for num in nums:
            result += abs(num - median)
        return result