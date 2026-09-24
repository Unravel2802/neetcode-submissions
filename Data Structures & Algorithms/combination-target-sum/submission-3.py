class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(idx, total):
            if total == target:
                res.append(cur[:])
                return

            if total > target or idx == len(nums):
                return 

            cur.append(nums[idx])
            backtrack(idx, total + nums[idx])
            cur.pop()
            backtrack(idx + 1, total)
        
        backtrack(0, 0)
        return res