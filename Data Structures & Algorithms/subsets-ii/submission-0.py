class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def dfs(i):
            if i >= len(nums):
                if cur not in res:
                    res.append(cur.copy())
                return 
            
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)
        
        dfs(0)
        return res