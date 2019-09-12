class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or coins is None or len(coins) == 0:
            return 0
        dp = [0] * (amount + 1)
        for coin in coins:
            for i in range(coin, amount + 1):
                if i == coin:
                    dp[i] = 1
                elif dp[i] == 0 and dp[i - coin] != 0:
                    dp[i] = dp[i - coin] + 1
                elif dp[i - coin] != 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return -1 if dp[amount] == 0 else dp[amount]
        
a=Solution()
print(a.coinChange("3+2*2"))