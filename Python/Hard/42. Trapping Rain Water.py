class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        
        ans = 0
        while left < right:
            max_left, max_right = max(height[left], max_left), max(height[right], max_right)
            if max_left <= max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1
        
        return ans