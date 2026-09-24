class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            for j in range(i-1):
                dp[i] = max(dp[i-1], dp[j] + nums[i])

        print(dp)
        return dp[-1]