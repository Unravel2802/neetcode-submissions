class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time = 0 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            rotten = len(q)
            for _ in range(rotten):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    return -1
        return max(time - 1, 0)