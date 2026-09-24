class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Intuition:
        # Sort intervals by start.
        # The result keeps already merged intervals.
        # If current interval overlaps with the last one in result,
        # merge them by extending the end.
        # Otherwise, append it as a new interval.

        intervals.sort(key=lambda x: x[0])
        merged = []

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged