class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection
        graph = defaultdict(list)

        for num1, num2 in edges:
            graph[num1].append(num2)
            graph[num2].append(num1)

        visited = set()
        def dfs(num, parent):
            if num in visited:
                return False
            
            visited.add(num)

            for neighbor in graph[num]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, num):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n