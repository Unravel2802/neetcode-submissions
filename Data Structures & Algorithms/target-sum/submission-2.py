class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 1. State: dp[i][j] = number of ways to reach sum j using the first i numbers
        # 2. TransitionL dp[i][j] = dp[i - 1][j - x] + dp[i - 1][j + x]

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            x = nums[i - 1]

            for s, count in dp[i - 1].items():
                dp[i][s + x] += count
                dp[i][s - x] += count
            
        return dp[n][target]