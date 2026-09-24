class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)

        visiting, visited = set(), set()

        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True

            visiting.add(c)
            for p in graph[c]:
                if not dfs(p):
                    return False
            
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
