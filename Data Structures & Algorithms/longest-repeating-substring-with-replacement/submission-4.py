class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        count_freq = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            count_freq[s[right]] += 1
            max_freq = max(max_freq, count_freq[s[right]])

            while (right - left + 1) - max_freq > k:
                count_freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res