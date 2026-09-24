from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        have = 0
        need_count = len(need)

        res_len = float("inf")
        res_left = 0

        left = 0

        for right, ch in enumerate(s):
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_count:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_left = left

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        if res_len == float('inf'):
            return ""

        return s[res_left : res_left + res_len]