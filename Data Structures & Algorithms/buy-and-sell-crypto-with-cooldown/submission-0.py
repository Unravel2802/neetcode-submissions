class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Idea:
        # At each day, either do nothing, buy, or sell.
        # If we sell on day i, then day i + 1 is cooldown,
        # so the next state starts at i + 2.
        # Use memoization on (day, can_buy).

        n = len(prices)
        memo = {}
    
        def dfs(i, buying):
            if i >= n:
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            
            return memo[(i, buying)]
        return dfs(0, True)