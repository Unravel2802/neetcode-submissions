class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temp)
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                res[stack[-1][0]] = idx - stack[-1][0]
                stack.pop()
            
            stack.append((idx, temp))
        
        return res
