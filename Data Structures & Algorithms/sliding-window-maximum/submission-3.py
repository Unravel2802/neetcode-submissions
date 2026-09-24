from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition:
        We want the max of every window of size k efficiently.
        A max-heap works but is O(n log n) with lazy deletion complexity.
        
        Better: Monotonic Decreasing Deque.
        - Deque stores INDICES, values represented are always decreasing front→back
        - Front = index of current window's maximum
        - Before inserting new element: pop from back anything SMALLER (they're 
          dominated — can never be a max while new element is in the window)
        - After inserting: pop from front if that index has left the window
        
        This gives O(1) amortized per element since each index is 
        pushed and popped at most once.
        
        Time:  O(n) — each element added/removed from deque at most once
        Space: O(k) — deque holds at most k indices
        """
        dq = deque()   # stores indices, decreasing by value front → back
        res = []

        for i in range(len(nums)):
            # Step 1: remove from back all indices whose values are
            #         <= nums[i] (they're useless — nums[i] dominates them)
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Step 2: remove front if it's outside the current window
            if dq[0] < i - k + 1:
                dq.popleft()

            # Step 3: once we've seen at least k elements, record max
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res