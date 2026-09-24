class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        res = [0] * len(temperatures)
        # stack: monotonic stack of temperature indexes
        stack = []
        # idea: if the next temp is larger than temperature at stack[-1], pop the stack,
        # and the res[stack[i]
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)
        return res