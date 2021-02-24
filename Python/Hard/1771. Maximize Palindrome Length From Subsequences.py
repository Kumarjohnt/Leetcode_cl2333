from functools import lru_cache
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        word = word1 + word2
        n = n1 + n2
        
        @lru_cache(None)
        def helper(l, r, flag1, flag2):
            if r < n1 and not flag2:
                return -float('inf')
            if l >= n1 and not flag1:
                return -float('inf')
            if l == r:
                return 1
            if l > r:
                return 0
        
            if word[l] == word[r]:
                flag1 = flag1 or (l < n1)
                flag2 = flag2 or (r >= n1)
                return 2 + helper(l + 1, r - 1, flag1, flag2)
            else:
                return max(helper(l, r - 1, flag1, flag2), helper(l + 1, r, flag1, flag2))
            
            
        
        res = helper(0, n - 1, False, False)
        helper.cache_clear()
        return max(0, res)
        
        
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        m, n, ans = len(word1), len(word2), 0
        
        dp = [[0] * (m + n) for _ in range(m + n)]
        for j in range(m + n):
            dp[j][j] = 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 2 if i + 1 == j else dp[i+1][j-1] + 2
                    if i < m and j >= m: ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return ans   