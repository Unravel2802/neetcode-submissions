class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in dic:
                j = dic[comp]
                return [j, i]
            dic[num] = i 