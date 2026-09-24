class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Idea:
        # Find the sum of the nums, target is sum//2. Search for
        # the subsets that sum to sum//2
        # -> backtracking problem
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target] 
