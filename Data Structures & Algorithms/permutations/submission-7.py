class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for j in range(len(nums)):
                if nums[j] in path:
                    continue
                
                path.append(nums[j])
                dfs()
                path.pop()


        dfs()
        return res
