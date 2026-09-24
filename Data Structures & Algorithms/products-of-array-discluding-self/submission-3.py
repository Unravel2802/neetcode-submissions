class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 1 2 8
        # 48 24 6 1 

        left = [1]
        for idx in range(1, len(nums)):
            left.append(left[-1] * nums[idx - 1])
        
        right = [1]
        for idx in range(len(nums) - 2, -1, -1):
            right.append(right[-1] * nums[idx + 1])
        right = right[::-1]
        
        res = []
        for idx in range(len(nums)):
            res.append(left[idx] * right[idx])
        
        return res