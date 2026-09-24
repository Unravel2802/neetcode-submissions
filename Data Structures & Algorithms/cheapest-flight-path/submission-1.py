class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in flights:
            adj[u].append((v, w))

        heap = [(0, src, 0)]
        visited = {}

        while heap:
            w1, n1, stop = heapq.heappop(heap)

            if n1 == dst:
                return w1

            if stop > k:
                continue 

            if n1 in visited and visited[n1] <= stop:
                continue
            
            visited[n1] = stop

            for n2, w2 in adj[n1]:
                heapq.heappush(heap, (w1 + w2, n2, stop + 1))
        
        return -1