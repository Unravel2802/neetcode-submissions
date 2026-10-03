class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_cost = float('inf')
        for price in prices:
            max_profit = max(max_profit, price - min_cost)
            min_cost = min(min_cost, price)
        
        return max_profit