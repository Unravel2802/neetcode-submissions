class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        print(intervals)
        count = 0
        
        last = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < last[1]:
                count += 1
                if intervals[i][1] < last[1]:
                    last = intervals[i]
            else:
                last = intervals[i]
        
        return count