class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Intuition:
        Find the smallest substring of s containing all chars of t.
        Use variable-size sliding window: expand right to find a valid
        window, then shrink left to minimize it, record the minimum.

        Approach:
        - need: frequency map of t
        - have: frequency map of current window
        - match: count of chars where have[c] >= need[c]
        - required: number of unique chars in t that must be satisfied
        - Expand right: when a char hits its needed count, match += 1
        - When match == required: record window, shrink from left
        - Shrink left: when removing a char drops below needed, match -= 1

        Time:  O(|s| + |t|)  — each char added/removed at most once
        Space: O(|s| + |t|)  — for the frequency maps
        """
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        match = 0
        required = len(need)          # unique chars in t we must satisfy

        best_len = float("inf")
        best_left = 0

        left = 0
        for right in range(len(s)):
            # --- Expand: add s[right] to window ---
            c = s[right]
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                match += 1            # just satisfied this char's requirement

            # --- Shrink: try to move left while window is valid ---
            while match == required:
                # Record if this is the best window so far
                if (right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_left = left

                # Remove s[left] from window
                left_c = s[left]
                have[left_c] -= 1
                if left_c in need and have[left_c] < need[left_c]:
                    match -= 1        # no longer satisfying this char
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_left : best_left + best_len]