class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        res = []

        while q:
            course = q.popleft()
            res.append(course)
        
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []