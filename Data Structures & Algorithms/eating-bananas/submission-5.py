class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        # binary search on the number of bananas to eat per hour
        # from 1 to max(piles) 
        while low < high:
            k = (low + high) // 2

            time = 0
            for pile in piles:
                time += (pile + k - 1) // k
            
            if time > h:
                low = k + 1
            else:
                high = k
        
        return low