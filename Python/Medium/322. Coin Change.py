class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0
        
        for coin in coins:
            for j in range(coin, amount + 1):
                if dp[j - coin] != float('inf'):
                    dp[j] = min(dp[j], dp[j - coin] + 1)
        
        return -1 if dp[amount] == float('inf') else dp[amount]
        
        