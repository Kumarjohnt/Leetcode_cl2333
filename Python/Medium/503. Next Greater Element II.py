class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, result = [], [-1] * len(nums)
        for i, num in enumerate(nums + nums):
            while stack and stack[-1][1] < num:
                idx, val = stack.pop()
                if idx < len(nums):
                    result[idx] = num
            stack.append((i, num))
        
        
        return result