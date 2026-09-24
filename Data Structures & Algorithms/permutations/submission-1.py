class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = set()
        def backtrack(i):
            if i == len(nums):
                res.append(cur.copy())
                return 
            
            for num in nums:
                if num in used:
                    continue
                cur.append(num)
                used.add(num)
                backtrack(i + 1)
                cur.pop()
                used.remove(num)

        backtrack(0)
        return res