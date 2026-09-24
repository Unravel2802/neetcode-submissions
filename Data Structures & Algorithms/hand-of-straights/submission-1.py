from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Intuition:
        # The smallest unused card must start a group.
        # If a card x appears c times and is the smallest remaining,
        # then we must start c groups from x.
        # So x, x+1, ..., x+groupSize-1 must each appear at least c times.

        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)

        for x in sorted(count):
            if count[x] > 0:
                need = count[x]   # number of groups that must start at x

                for nxt in range(x, x + groupSize):
                    if count[nxt] < need:
                        return False
                    count[nxt] -= need

        return True