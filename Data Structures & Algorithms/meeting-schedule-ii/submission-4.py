"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort()
        rooms = 0
        res = 0

        for time, delta in events:
            rooms += delta
            res = max(res, rooms)
        
        return res 