class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in num:
            while stack and k > 0 and i < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)
            
        while k > 0:
            stack.pop()
            k -= 1
        
        return "".join(stack).lstrip("0") or "0"