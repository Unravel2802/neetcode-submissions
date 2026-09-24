class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n
        res = 0

        # left max calculation:
        left[0] = height[0]
        for idx in range(1, n):
            left[idx] = max(height[idx], left[idx - 1])
        
        # right max calculation:
        right[-1] = height[-1]
        for idx in range(n - 2, -1, -1):
            right[idx] = max(height[idx], right[idx + 1])
        
        # calculate the water trap at each index based on the 
        # max left and right bars
        for idx in range(n):
            res += (min(left[idx], right[idx]) - height[idx])
    
        return res