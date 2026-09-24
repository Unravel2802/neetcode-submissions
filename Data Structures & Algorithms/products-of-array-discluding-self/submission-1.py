class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix
        res = []
        prefix = [1]
        suffix = [1]
        n = len(nums)

        for i in range(n-1):
            prefix.append(nums[i] * prefix[i])

        # 1, 1, 2, 8
        # 1, 6, 24, 48
        # 48, 24, 6, 1 

        for i in range(n-1, 0, -1):
            suffix.append(nums[i] * suffix[-1])
        
        suffix.reverse()
        for i in range(n):
            res.append(prefix[i] * suffix[i])

        return res