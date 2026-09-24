class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Intuition:
        # Maintain tails where tails[i] is the smallest possible tail
        # of an increasing subsequence of length i + 1.
        # For each num:
        # - if num is bigger than all tails, append it
        # - otherwise replace the first tail >= num
        # This keeps future extension opportunities as large as possible.

        tails = []

        for num in nums:
            left, right = 0, len(tails)

            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)