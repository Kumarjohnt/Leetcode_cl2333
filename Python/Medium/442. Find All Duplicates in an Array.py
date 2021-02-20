class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            if num < 0:
                idx = -num - 1
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
                else:
                    result.append(-num)
            else:
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
                else:
                    result.append(num)
        return result
        
        
                
        
        