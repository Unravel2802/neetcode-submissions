class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def backtrack(i, total):
            if total == target:
                res.append(cur[:])
                return 
            
            if total > target or i > len(nums):
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                cur.append(nums[j])
                backtrack(j + 1, total + nums[j])
                cur.pop()
        
        backtrack(0, 0)
        return res