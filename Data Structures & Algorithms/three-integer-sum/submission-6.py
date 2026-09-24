class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for idx in range(n - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            if nums[idx] > 0:
                return res
        
            left, right = idx + 1, n - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[idx], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return res