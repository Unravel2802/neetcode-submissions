class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        # When is the target in the left half?
        # -> mid > target and target > low -> left half is increasing 
        # 
        while low <= high:
            mid = (low + high) // 2

            # Target found:
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                # Target is in the left half 
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                # Target is in the right half
                else:
                    low = mid + 1

            else:
                # Target is in the right half
                if nums[high] >= target >= nums[mid]:
                    low = mid + 1
                # Target is in the left half 
                else:
                    high = mid - 1
            
        return -1