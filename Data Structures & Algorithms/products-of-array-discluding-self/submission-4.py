class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 1, 2, 8
        # 48, 24, 6, 1

        n = len(nums)

        left, right = [0] * n, [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        right[-1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
                
        res = []
        for i in range(n):
            res.append(left[i] * right[i])
        
        return res