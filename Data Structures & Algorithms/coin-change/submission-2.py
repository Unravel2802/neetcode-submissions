class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            if rem == 0:
                return 0
            
            if rem < 0:
                return float('inf')

            if rem in memo:
                return memo[rem]

            
            res = float('inf')

            for coin in coins:
                res = min(res, 1 + dfs(rem - coin))
            
            memo[rem] = res
            return res
        
        ans = dfs(amount)
        return ans if ans != float('inf') else -1