class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        result = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]: 
                left = stack.pop()
                h = heights[left]
                w = i - stack[-1] - 1
                result = max(result, w * h)
            stack.append(i)
        heights.pop()
        return result