
#INEFFICIENT DFS APPROACH
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c, steps, visited):
            # ❌ BASE CASE: If out of bounds or invalid cell
            if (
                r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == -1 or (r, c) in visited
            ):
                return float('inf')  # unreachable

            # ✅ BASE CASE: Found a treasure
            if grid[r][c] == 0:
                return steps

            visited.add((r, c))  # mark current as visited

            min_steps = float('inf')

            for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                dist = dfs(nr, nc, steps + 1, visited)
                min_steps = min(min_steps, dist)

            visited.remove((r, c))  # backtrack

            return min_steps

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == INF:
                    res = dfs(i, j, 0, set())
                    if res != float('inf'):
                        grid[i][j] = res
