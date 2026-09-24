class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for c, p in prerequisites:
            graph[c].append(p)

        visiting = set()
        visited = set()
    
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True