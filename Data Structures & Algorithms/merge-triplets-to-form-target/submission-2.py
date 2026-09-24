class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False, False, False]

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]:
                    good[0] = True
                if b == target[1]:
                    good[1] = True
                if c == target[2]:
                    good[2] = True
        
        return good[0] and good[1] and good[2]