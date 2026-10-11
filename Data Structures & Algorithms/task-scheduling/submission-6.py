class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequencies
        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1

        # Max heap using negative frequencies
        heap = [-freq for freq in dic.values()]
        heapq.heapify(heap)

        # (remaining frequency, next available time)
        q = deque()

        time = 0

        while heap or q:
            time += 1

            # Execute the most frequent available task
            if heap:
                freq = heapq.heappop(heap)
                freq += 1  # Negative frequency moves toward zero

                # Task still has remaining occurrences
                if freq < 0:
                    q.append((freq, time + n))

            # Check whether a task has finished cooling down
            if q and q[0][1] <= time:
                freq, avail = q.popleft()
                heapq.heappush(heap, freq)

        return time