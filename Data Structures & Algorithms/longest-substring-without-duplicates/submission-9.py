class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mp = {}
        longest = 0

        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            
            mp[s[right]] = right
            longest = max(longest, right - left + 1)
        
        return longest