class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i):
            if i == len(nums):
                res.append(cur.copy())
                return 
            
            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                backtrack(i + 1)
                cur.pop()

        backtrack(0)
        return res