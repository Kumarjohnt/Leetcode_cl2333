class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        n = len(nums)
        result = n * [-1]
        
        for num in nums:
            if 0 < num <= n:
                result[num - 1] = 1
        
        for i in range(n):
            if result[i] == -1:
                return i + 1
        
        return n + 1
            
        