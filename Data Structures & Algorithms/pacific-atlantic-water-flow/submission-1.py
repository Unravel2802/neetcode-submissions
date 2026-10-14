class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific, atlantic = set(), set()


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visited):
            if (r, c) in visited:
                return 
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    heights[nr][nc] < heights[r][c]):
                    continue
                
                dfs(nr, nc, visited)


        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        
        res = []
    
        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])

        return res 
