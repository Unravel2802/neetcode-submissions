class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def backtrack(idx, total):
            if total == target:
                res.append(cur[:])
                return 
            
            if total > target or idx > len(nums):
                return
            
            for nxt in range(idx, len(nums)):
                if nxt > idx and nums[nxt] == nums[nxt - 1]:
                    continue

                cur.append(nums[nxt])
                backtrack(nxt + 1, total + nums[nxt])
                cur.pop()
        
        backtrack(0, 0)
        return res