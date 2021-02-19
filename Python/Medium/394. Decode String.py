class Solution:
    def decodeString(self, s: str) -> str:
        
        num, stack, string = 0, [], ""
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            
            elif c == "[":
                stack.append(string)
                stack.append(num)  
                num, string = 0, ""
                
            
            elif c == "]":
                n = stack.pop()
                prev_string = stack.pop()
            
                string = prev_string + n * string
                
            else:
                string += c
                
        return string
        
            
            