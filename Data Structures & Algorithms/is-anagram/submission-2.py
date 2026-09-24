class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)

        for ch in s:
            dic[ch] += 1

        for ch in t:
            dic[ch] -= 1
        
        for key, value in dic.items():
            if value != 0:
                return False
        
        return True