class Solution:
    def trap(self, height: List[int]) -> int:
        # dp
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        res = 0

        for i in range(n):
            if i > 0:
                left_max[i] = max(height[i], left_max[i-1])
            else:
                left_max[i] = height[i]

        for i in range(n-1, -1, -1):
            if i < n-1:
                right_max[i] = max(height[i], right_max[i+1])
            else:
                right_max[i] = height[i]
            
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]

        return res