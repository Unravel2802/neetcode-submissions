class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] = maximum profit starting from day i when we can BUY
        # dp[i][1] = maximum profit starting from day i when we can SELL
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(-prices[i] + dp[i + 1][1], dp[i + 1][0])
            dp[i][1] = max(prices[i] + dp[i + 2][0], dp[i + 1][1])
        
        return dp[0][0]