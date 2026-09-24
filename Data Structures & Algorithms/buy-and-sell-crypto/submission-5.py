class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = float('inf')
        profit = 0

        for price in prices:
            prev = min(prev, price)
            profit = max(profit, price - prev)
        
        return profit