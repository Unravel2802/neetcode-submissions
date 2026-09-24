from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        left = 0
        res = 0
        max_freq = 0

        for right, ch in enumerate(s):
            dic[ch] += 1
            max_freq = max(max_freq, dic[ch])

            while (right - left + 1) - max_freq > k:
                dic[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res