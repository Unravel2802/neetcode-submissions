class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        res = []
        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
            print(len(res), i)
            if len(res) < i + 1:
                res.append(0)
        res.append(0)
        return res