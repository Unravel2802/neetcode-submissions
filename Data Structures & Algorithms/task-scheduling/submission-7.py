class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Start with the task with most frequency
        # Convert the list of tasks to heap sorted by frequency of the task with an idle time
        # Sort by availability then frequency? 
        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1
        
        heap = [-freq for freq in dic.values()]
        heapq.heapify(heap)
        
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                freq += 1
            
                if freq < 0:
                    q.append((freq, time + n))

            if q and q[0][1] <= time:
                freq, avail = q.popleft()
                heapq.heappush(heap, freq)

        return time 

            