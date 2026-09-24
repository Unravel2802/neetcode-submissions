class Solution:
    def trap(self, height: List[int]) -> int:
        # Questions: 
        # Edges cases: What are some possible edge cases (empty height list, all heights are 0)
        

        # Approach: prefix and suffix array
        # Create a left maximum and a right maximum array to store the maximum left and right 
        # height at a point.

        water = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        # 1. Find left max:
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        # 2. Find right max:
        right_max[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(n):
            water = water + (min(left_max[i], right_max[i]) - height[i])
        
        return water