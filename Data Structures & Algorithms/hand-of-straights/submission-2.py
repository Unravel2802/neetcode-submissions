class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Starting at card x, for the next x + k cards, those cards number must be >= card x 
        n = len(hand)

        if n % groupSize != 0:
            return False
        
        hand.sort()
        counter = Counter(hand)

        for x in hand:
            if counter[x] == 0:
                continue
            
            for j in range(x, x + groupSize):
                if counter[j] == 0:
                    return False
                
                counter[j] -= 1

        return True