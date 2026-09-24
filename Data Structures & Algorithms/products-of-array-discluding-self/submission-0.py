class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            prod = 1
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                prod *= num2
            res.append(prod)
        return res