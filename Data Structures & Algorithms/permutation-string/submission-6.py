class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        s2Count = [0] * 26
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        for idx in range(n1):
            s1Count[ord(s1[idx]) - ord('a')] += 1
            s2Count[ord(s2[idx]) - ord('a')] += 1
        
        match = 0
        for idx in range(26):
            match += (1 if s1Count[idx] == s2Count[idx] else 0)
        
        left = 0
        for right in range(n1, n2):
            if match == 26:
                return True
        
            rIndex = ord(s2[right]) - ord('a')
            s2Count[rIndex] += 1
            if s2Count[rIndex] == s1Count[rIndex]:
                match += 1
            elif s2Count[rIndex] - 1 == s1Count[rIndex]:
                match -= 1
            
            lIndex = ord(s2[left]) - ord('a')
            s2Count[lIndex] -= 1
            if s2Count[lIndex] == s1Count[lIndex]:
                match += 1
            elif s2Count[lIndex] + 1 == s1Count[lIndex]:
                match -= 1
        
            left += 1
        return match == 26
