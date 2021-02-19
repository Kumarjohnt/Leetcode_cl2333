from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, count = 0, 0
        freq = Counter(t)
        ans = ""
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] -= 1
                if freq[s[right]] >= 0:
                    count += 1
            
            while count == len(t):
                if not ans or right - left + 1 < len(ans):
                    ans = s[left : right + 1]
                
                if s[left] in freq:
                    freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count -= 1
                
                left += 1
        
        return ans