class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        cur = []
        def backtrack(idx):
            if idx == len(nums):
                if cur not in res:
                    res.append(cur[:])
            
            for nxt in range(idx, len(nums)):
                if nxt > idx and nums[nxt] == nums[nxt - 1]:
                    continue
                
                cur.append(nums[nxt])
                backtrack(nxt + 1)
                cur.pop()
                backtrack(nxt + 1)
                
        backtrack(0)
        return res