class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # idea: either take or skip a number
        res = []
        cur = []
        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1)
            
            # backtrack
            cur.pop()

            # continue with the search
            dfs(i + 1)
        
        dfs(0)
        return res

