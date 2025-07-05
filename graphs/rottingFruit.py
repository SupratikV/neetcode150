class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        q=deque()
        min=0
        fresh=0
        rot=0
        inirot=0

        def addBanana(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c]==2 or grid[r][c]==0 or (r,c) in visited:
                return
            q.append((r,c))
            visited.add((r,c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:#rotten fruit found
                    q.append((i,j))
                    visited.add((i,j))
                    inirot+=1
                elif grid[i][j]==1:
                    fresh+=1

        if inirot==0 and fresh==0:
            return 0
        
        #start logic
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=2
                rot+=1
                addBanana(r+1,c)
                addBanana(r-1,c)
                addBanana(r,c+1)
                addBanana(r,c-1)
            min+=1
        print(grid)
        if fresh<rot:
            return min-1
        else:
            return -1


        