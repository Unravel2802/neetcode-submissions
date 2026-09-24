class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        max_water = 0

        while left < right:
            min_height = min(heights[left], heights[right])
            max_water = max(max_water, min_height * (right - left))
        
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water