import heapq

class MedianFinder:
    """
    Intuition:
    Use two heaps:
    - small: max-heap (store negatives) for the smaller half
    - large: min-heap for the larger half

    Keep them balanced so their sizes differ by at most 1.
    Also ensure every number in small <= every number in large.

    Then:
    - if one heap has more elements, its top is the median
    - if both heaps have equal size, median is the average of both tops
    """

    def __init__(self):
        self.small = []  # max-heap via negatives
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # Step 1: push into small first
        heapq.heappush(self.small, -num)

        # Step 2: make sure ordering is valid
        # largest in small should not be greater than smallest in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: rebalance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (-self.small[0] + self.large[0]) / 2