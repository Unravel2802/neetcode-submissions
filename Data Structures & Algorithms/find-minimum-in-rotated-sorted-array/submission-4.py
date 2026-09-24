class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Idea:
        # The array was originally sorted but rotated.
        # The minimum element is where the rotation happened.
        # Use binary search:
        # If nums[mid] < nums[right], the minimum is in the left half (including mid).
        # Otherwise the minimum is in the right half.

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]