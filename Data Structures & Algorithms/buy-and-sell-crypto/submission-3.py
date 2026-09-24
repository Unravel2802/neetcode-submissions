class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = float('inf')
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - best_buy)
            best_buy = min(best_buy, price)
        
        return max_profit
