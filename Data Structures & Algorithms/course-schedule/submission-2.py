class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Questions
        # 1. Can the number of courses be 0?
        # 2. Can the course number be negative?
    
        # Each prerequisite pair [a, b] is equal to
        # an edge going from b to a -> directed graph 
        # because we need to finish b before getting a

        # If this directed graph has a cycle, 
        # then we cannot reach all the nodes in the graph

        # Optimal Solution: BFS, topological sort

        # Idea:
        # Build the adjacency list for the prerequisites and the courses
        # Calculate the indegree of every course, indegree = how many prerequisits
        # are required
        # Put every course with indegree 0 into a queue
        # Pop the queue and reduce the indegree of the neighbors
        # If a neighbor indegree becomes 0, we push it into the queue.
        # Count how many courses we are able to process
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # start with all courses that have indegree of 0:
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        taken = 0

        while q:
            course = q.popleft()
            taken += 1
        
            # Process the courses in topological order
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
            
        return taken == numCourses


