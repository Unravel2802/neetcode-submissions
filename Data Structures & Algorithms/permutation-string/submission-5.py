class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isPermu(s1, s2):
            count = Counter(s1)
            for ch in s2:
                count[ch] -= 1
            
            for key, val in count.items():
                if val != 0:
                    return False
            
            return True
        
        m, n = len(s1), len(s2)
        for i in range(n - m + 1):
            if isPermu(s1, s2[i : i + m]):
                return True
        
        return False