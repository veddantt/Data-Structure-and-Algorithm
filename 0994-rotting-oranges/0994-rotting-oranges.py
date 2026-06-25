class Solution(object):
    def orangesRotting(self, grid):
        m, n, fresh, q = len(grid), len(grid[0]), 0, deque()
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions, minutes = [(0,1), (1,0), (0,-1), (-1,0)], 0
        while q:
            r, c, minutes = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc], fresh = 2, fresh - 1
                    q.append((nr, nc, minutes + 1))
        
        return minutes if fresh == 0 else -1      