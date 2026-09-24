class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        count = 0
        
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if prev > start:
                count += 1
                prev = min(prev, end)
            
            else:
                prev = end
        
        return count