class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        match = 0

        for i in range(26):
            match += 1 if count1[i] == count2[i] else 0
        
        left = 0
        for right in range(len(s1), len(s2)):
            if match == 26:
                return True
            
            left_char = ord(s2[left]) - ord('a')
            if count2[left_char] == count1[left_char]:
                match -= 1
            count2[left_char] -= 1
            if count2[left_char] == count1[left_char]:
                match += 1

            right_char = ord(s2[right]) - ord('a')
            if count2[right_char] == count1[right_char]:
                match -= 1
            count2[right_char] += 1
            if count2[right_char] == count1[right_char]:
                match += 1
            
            left += 1
        return match == 26

