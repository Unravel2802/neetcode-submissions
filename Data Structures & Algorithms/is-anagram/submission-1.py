class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        
        for c in t:
            dic[c] -= 1

        for key, val in dic.items():
            if val != 0:
                return False
        
        return True 