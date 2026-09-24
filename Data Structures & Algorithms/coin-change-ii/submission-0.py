class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Idea:
        # Calculate the number of ways to make from 1 to amount - 1

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for target in range(coin, amount + 1):
                dp[target] += dp[target - coin]


        return dp[amount]

        
