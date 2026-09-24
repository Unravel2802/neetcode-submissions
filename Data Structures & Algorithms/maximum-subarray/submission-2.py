class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Idea:
        # dp[i] = maximum subarray sum ending exactly at index i
        # For each index:
        # 1. start a new subarray at nums[i]
        # 2. extend the previous subarray
        # Take the best over all dp[i]

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [float('-inf')] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])

        return max(dp)