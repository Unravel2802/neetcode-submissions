class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        adj = defaultdict(list)

        for u, v, cst in flights:
            adj[u].append([v, cst])

        q = deque([(0, src, 0)])

        while q:
            cost, node, stops = q.popleft()
            if stops > k:
                continue
            
            for neighbor, w in adj[node]:
                nextCost = cost + w
                if nextCost < prices[neighbor]:
                    prices[neighbor] = nextCost
                    q.append((nextCost, neighbor, stops + 1))
            
        return prices[dst] if prices[dst] != float('inf') else -1