class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest consecutive sequence
        if len(nums) == 0:
            return 0 
        nums.sort()
        max_window = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] - nums[i-1] > 1:
                max_window = max(max_window, count)
                count = 1
        max_window = max(max_window, count)
        return max_window