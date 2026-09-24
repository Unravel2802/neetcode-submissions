class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        n = len(height)

        for i in range(1, n - 1):
            left = 0
            right = 0
            for j in range(i, -1, -1):
                left = max(left, height[j])

            for j in range(i, n):
                right = max(right, height[j])
            water += min(left, right) - height[i]

        return water