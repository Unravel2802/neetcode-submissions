class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Idea:
        # Use backtracking with swapping.
        # At index i, try every element from i..n-1 in that position.
        # Swap, recurse to fill the next index, then swap back to restore state.

        res = []

        def backtrack(i):
            # Base case: a full permutation is formed
            if i == len(nums):
                res.append(nums[:])
                return

            # Try every candidate for position idx
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]  # choose
                backtrack(i + 1)                       # explore
                nums[i], nums[j] = nums[j], nums[i]  # unchoose

        backtrack(0)
        return res