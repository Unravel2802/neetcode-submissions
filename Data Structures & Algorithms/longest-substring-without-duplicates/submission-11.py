class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_seen = {}
        max_len = 0

        for right in range(len(s)):
            if s[right] in last_seen:
                left = max(left, last_seen[s[right]] + 1)
            
            last_seen[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len