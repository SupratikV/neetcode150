from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        q = deque()
        island = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            q.append((r, c))
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
                for nr, nc in directions:
                    new_r, new_c = r + nr, c + nc
                    if (0 <= new_r < rows and 0 <= new_c < cols and
                        (new_r, new_c) not in visited and grid[new_r][new_c] == "1"):
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    island += 1

        return island
