class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Idea:
        # Binary search the eating speed k.
        # If Koko eats at speed k, we can compute how many total hours she needs.
        # If total hours <= h, then k works, so try smaller.
        # Otherwise, k is too slow, so try bigger.

        l, r = 1, max(piles)
        k = r

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += (p + m - 1) // m  

            if totalTime <= h:
                k = m
                r = m - 1
            else:
                l = m + 1

        return k