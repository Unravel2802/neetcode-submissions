class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i, num in enumerate(nums):
            remain = target - num
            if remain in seen.keys():
                return [seen[remain], i]
            
            seen[num] = i
    