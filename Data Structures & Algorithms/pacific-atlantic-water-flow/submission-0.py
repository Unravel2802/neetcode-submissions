class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        pacific, atlantic = set(), set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visit or 
                    heights[nr][nc] < heights[r][c]):
                    continue
                dfs(nr, nc, visit)
        
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)
            dfs(r, 0, pacific)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])     

        return res       