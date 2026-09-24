class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        total = 0
        def dfs(node, visiting):
            visited.add(node)
            visiting.add(node)
            for nei in graph[node]:
                if nei not in visiting:
                    dfs(nei, visiting)
        for num in range(n):
            if num not in visited:
                visiting = set()
                dfs(num, visiting)
                total += 1

        return total