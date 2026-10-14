class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False
        
        for u, v in edges:
            if dfs(u, v, set()):
                return [u, v]
            
            graph[u].append(v)
            graph[v].append(u)
            
        return []