class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, jump):
            if i >= n - 1:
                return jump

            farthest = min(n - 1, i + nums[i])
            
            if farthest == n - 1:
                return jump + 1

            max_index = i + 1
            max_reach = max_index + nums[max_index]

            for j in range(i + 1, farthest + 1):
                if j + nums[j] >= max_reach:
                    max_reach = j + nums[j] 
                    max_index = j

            return dfs(max_index, jump + 1)
        return dfs(0, 0)