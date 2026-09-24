class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        mp = {}
        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            
            mp[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
