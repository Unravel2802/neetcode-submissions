class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Given an array of integers and an integer targer
        # 2 choices: either add or subtract it from the total sum
        # [1, 1] -> + 1 - 1 = 0 or - 1 + 1 = 0
        # Find the number of different ways to make the target

        # Question: do I have to use all the number in the list? 
        # what are the constraints (like nums length, number value and target value)

        # Idea:
        # Since this a problem that I need to find the total number of ways, we need to 
        # use backtracking. And with given constraints, I think that we need to use
        # some dp memoization to optimize.

        # First, I will start with just backtracking then I will add the dp memoization later.
        # Now, my run time is O(n^2) because I'm searching for all possible combinations without
        # storing the old possible answer

        # How to store/use memoization? Use a dictionary of the index and the total number of ways 
        # to build target at that position ((i, total))
        memo = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in memo:
                return memo[(i, total)]

            add = dfs(i + 1, total + nums[i])
            subtract = dfs(i + 1, total - nums[i])
            memo[(i, total)] = add + subtract
            return memo[(i, total)]

        return dfs(0, 0) 

            