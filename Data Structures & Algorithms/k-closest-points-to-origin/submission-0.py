import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        res = []
        for x, y in points:
            distance = sqrt(x**2 + y ** 2)
            heapq.heappush(dist, (distance, [x, y]))

        while k > 0:
            distance, point = heapq.heappop(dist)
            res.append(point)
            k -= 1

        return res
