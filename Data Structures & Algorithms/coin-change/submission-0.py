class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Idea: 
        # Build the amounts that we can make from the coins from 1 to amount
        # At each number of amount, we will find the minimum number of 
        # coins we need to build it.
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
            
        for target in range(1, amount + 1):
            for coin in coins:
                if target - coin >= 0:
                    dp[target] = min(dp[target], dp[target - coin] + 1)
            
        return dp[amount] if dp[amount] != float('inf') else -1