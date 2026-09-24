from typing import List
import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Idea:
        # Sort meetings by start time.
        # Keep a min-heap of room end times.
        # If the earliest ending room is free, reuse it.
        # Otherwise, allocate a new room.
        
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if min_heap[0] <= start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap)