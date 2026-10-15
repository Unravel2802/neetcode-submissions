class Solution:
    def getDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)

        for i in range(n):
            for j in range(n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = self.getDistance(x1, y1, x2, y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        minHeap = [(0, 0)]
        res = 0
        visited = set()

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for neiCost, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        
        return res
