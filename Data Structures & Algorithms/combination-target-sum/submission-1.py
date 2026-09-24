class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i, total):
            if total > target or i >= len(nums):
                return
            
            if total == target:
                res.append(cur.copy())
                return             
            
            cur.append(nums[i])
            backtrack(i, total + nums[i])
            cur.pop()
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res

