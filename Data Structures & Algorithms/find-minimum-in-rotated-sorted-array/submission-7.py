class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # minimum is on the right half 
            if nums[mid] > nums[high]:
                low = mid + 1
            # minimum is on the left half
            else:
                high = mid 
        
        return nums[low]