class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # backtracking + dp (memoization)?
        memo = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            if i in memo:
                return memo[i]

            farthest = min(len(nums) - 1, i + nums[i])
            for num in range(i + 1, farthest + 1):
                if dfs(num):
                    memo[num] = True
                    return True
            return False

        return dfs(0)

        # need to add dp memoization