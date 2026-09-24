class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Given an array of Neetcoin prices and each index of the array represents the day number
        # I can choose to not make any transaction
        # I can only make one transaction

        min_price = float('inf')
        max_profit = 0
        for price in prices:    
            max_profit = max(max_profit, price - min_price)           
            min_price = min(min_price, price)
        
        return max_profit
