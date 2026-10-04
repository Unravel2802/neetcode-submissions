class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if n < m:
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(m):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            match += 1 if count1[i] == count2[i] else 0

        for i in range(m, n):
            if match == 26:
                return True

            # Remove the left letter of s2:
            left = ord(s2[i - m]) - ord('a')
            if count2[left] - 1 == count1[left]:
                match += 1
            elif count2[left] == count1[left]:
                match -= 1
            count2[left] -= 1
        
            # Add the right letter of s2:
            right = ord(s2[i]) - ord('a')
            if count2[right] +1 == count1[right]:
                match += 1
            elif count2[right] == count1[right]:
                match -=1
            count2[right] += 1
 
        return match == 26