class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [101] * n

        dp[0] = prices[0]

        max_profit = 0
        for i in range(1, n):
            dp[i] = min(prices[i], dp[i-1])
            max_profit = max(max_profit, prices[i] - dp[i-1])
        return max(max_profit, 0)
