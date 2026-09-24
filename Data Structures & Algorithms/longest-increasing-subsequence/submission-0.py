class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Idea:
        # Brute force: Try every subsequence using dfs
        # At each index, we have 2 choices:
        # 1. Skips nums[i]
        # 2. Take nums[i] only if it is greateer than the previous chosen number
        
        n = len(nums)
        
        def dfs(i, prev):
            if i == n:
                return 0
            
            res = dfs(i + 1, prev)

            if prev == -1 or nums[i] > nums[prev]:
                res = max(res, 1 + dfs(i + 1, i))
            
            return res
    
        return dfs(0, -1)