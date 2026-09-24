class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            comp = target - num
            if comp in dic:
                return [dic[comp] + 1, i + 1]
            dic[num] = i  