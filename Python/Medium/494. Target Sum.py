class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        memo = {}
        
        def recursive(index, cur_sum):
            
            if (index, cur_sum) in memo:
                return memo[(index, cur_sum)]
            
            if index == len(nums) and cur_sum == S:
                return 1
            elif index == len(nums):
                return 0
            
            positive = recursive(index + 1, cur_sum + nums[index])
            negative = recursive(index + 1, cur_sum - nums[index])
            
            memo[(index, cur_sum)] = positive + negative
            
            return memo[(index, cur_sum)] 
        
        return recursive(0, 0)
            