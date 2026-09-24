class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        INTUITION:
        For any bar, the max rectangle using that bar's height extends
        as far left and right as bars remain >= that height.
        A monotonic increasing stack lets us find both boundaries in O(1)
        amortized: when we pop a bar (current bar is shorter), we know:
          - right boundary = current index
          - left boundary  = new stack top (or -1 if empty)

        APPROACH: Monotonic Increasing Stack
        - Maintain stack of indices with increasing heights
        - On seeing a shorter bar: pop and compute area for the popped bar
        - Append sentinel height=0 to flush remaining elements cleanly

        COMPLEXITY:
        - Time:  O(n) — each bar pushed and popped at most once
        - Space: O(n) — stack

        EDGE CASES:
        - Single bar
        - All bars same height
        - Strictly increasing / strictly decreasing
        """
        heights.append(0)  # sentinel to flush stack at the end
        stack = [-1]       # seed with -1 to simplify left-boundary calc
        max_area = 0

        for i, h in enumerate(heights):
            # pop while current bar is shorter than stack top
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # restore original array (good practice)
        return max_area