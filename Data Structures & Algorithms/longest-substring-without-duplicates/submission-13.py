class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        maxlen = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)

            seen[s[right]] = right
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen