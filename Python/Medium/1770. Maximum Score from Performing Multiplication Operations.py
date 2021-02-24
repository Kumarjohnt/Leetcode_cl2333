from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        
        @lru_cache(None)
        def helper(i, j, idx):
            if idx == m:
                return 0
            
            r1 = multipliers[idx] * nums[i] + helper(i+1, j, idx+1)
            r2 = multipliers[idx] * nums[j] + helper(i, j-1, idx+1)
            
            return max(r1, r2)

        res = helper(0, n-1, 0)
        helper.cache_clear()
                    
        return res


class Solution {
int dp[1005][1005];  
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
      int n = nums.size(), m = multipliers.size(), res = -2e9;
      dp[0][0] = 0;
      for (int i = 1; i <= m; i++)
        for (int j = 0; j <= i; j++) {
          int ans = -2e9;
          if (j != 0)
            ans = max(ans, dp[i - 1][j - 1] + nums[j - 1] * multipliers[i - 1]);
          if (j != i)
            ans = max(ans, dp[i - 1][j] + nums[n - (i - j)] * multipliers[i - 1]);
          dp[i][j] = ans;
          if (i == m)
            res = max(res, ans);
        }
      return res;
    }
};

#讲解 bilibili.com/video/BV1QA411M7Da/