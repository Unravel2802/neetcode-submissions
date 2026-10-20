class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        res.append(newInterval)

        while i < n and intervals[i][0] <= res[-1][1]:
            start = min(intervals[i][0], res[-1][0])
            end = max(intervals[i][1], res[-1][1])
        
            res[-1] = [start, end]
            
            i += 1

        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res 