class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        left, right = 1, max_pile
        res = right

        while left < right:
            mid = left + (right - left) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid

            if time > h:
                left = mid + 1
            else:
                res = mid
                right = mid 
        
        return res