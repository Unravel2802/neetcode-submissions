class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        taken, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            taken += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return output[::-1] if taken == numCourses else []