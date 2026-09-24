class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i):
            if sum(cur) > target or i >= len(nums):
                return
            
            if sum(cur) == target:
                res.append(cur.copy())
                return             
            
            cur.append(nums[i])
            backtrack(i)
            cur.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res

