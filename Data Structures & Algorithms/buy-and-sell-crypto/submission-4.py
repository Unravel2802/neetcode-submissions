class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for idx in range(1, len(prices)):
            max_profit = max(max_profit, prices[idx] - min_price)
            min_price = min(min_price, prices[idx])
    
        return max_profit