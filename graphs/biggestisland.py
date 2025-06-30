class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=[]
        visited=set()
        rows=len(grid)
        cols=len(grid[0])

        def bfs(i,j):
            visited.add((i,j))
            q=deque()
            count=1
            q.append((i,j))
            while q:
                cr,cc=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for nr,nc in directions:
                    if (nr+cr) in range(rows) and (nc+cc) in range(cols) and grid[nr+cr][nc+cc]==1 and(nr+cr,nc+cc) not in visited:
                        visited.add((nr+cr,nc+cc))
                        q.append((nr+cr,nc+cc))
                        print("yes",count)
                        count+=1
            return count

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    c=bfs(i,j)
                    res.append(c)
        print(res)
        if res==[]:
            return 0
        return max(res)

        


# dfs code:
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area