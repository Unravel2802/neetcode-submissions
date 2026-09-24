class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Idea
        # subarray -> 2d dp -> dp[l][r] for best left and right positions of subarrays
        # cases:
        # 1. The subarray can be the number itself
        # 2. Continue to add numbers 
        # 3. start of a new subarray if the number is larger than the previous sub
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [float('-inf')] * (n + 1)
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        return max(dp)