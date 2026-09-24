class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last = {}
        max_len = 0 

        for right in range(len(s)):
            if s[right] in last:
                left = max(last[s[right]] + 1, left)

            last[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
