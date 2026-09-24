class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        # the maximum eating rate is the maximum value of the piles
        # bin search from 1 to max_pile to find the minimum eating rate
        # the condition to stop is when 
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else: 
                l = k + 1
        return res