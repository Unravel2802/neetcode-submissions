class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in nums and i != dic[target - nums[i]]:
                return [i, dic[target - nums[i]]]