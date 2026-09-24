class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Idea:
        # Binary search the eating speed k.
        # If Koko eats at speed k, we can compute how many total hours she needs.
        # If total hours <= h, then k works, so try smaller.
        # Otherwise, k is too slow, so try bigger.

        l, r = 1, max(piles)
        res = r

        while l < r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += (p + k - 1) // k  

            if totalTime <= h:
                res = k
                r = k 
            else:
                l = k + 1

        return res