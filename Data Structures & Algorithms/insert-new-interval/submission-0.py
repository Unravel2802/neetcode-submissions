class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Intuition:
        # Since intervals are sorted and non-overlapping, we only need one pass.
        # 1. Add all intervals ending before newInterval starts.
        # 2. Merge all overlapping intervals with newInterval.
        # 3. Add the merged newInterval, then append the rest.

        res = []
        i = 0
        n = len(intervals)

        # 1) intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2) merge overlaps
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        # 3) remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res