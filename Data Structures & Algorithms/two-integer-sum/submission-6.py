class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in mp:
                return [mp[comp], idx]
            mp[num] = idx
        
        return -1 