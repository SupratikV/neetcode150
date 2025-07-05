# We insert all the cells (row, col) that represent the treasure chests into the queue.
# Then, we process the cells level by level, handling all the current cells in the 
# queue at once. 
# For each cell, we mark it as visited and store the current level value as 
# the distance at that cell. We then try to add the neighboring cells (adjacent cells) 
# to the queue, but only if they have not been visited and are land cells.

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        visit=set()
        steps=0
        def addRoom(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c]==-1 or (r,c) in visit:
                return
            q.append((r,c))
            visit.add((r,c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j))
                    visit.add((i,j))
        #start bfs
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=steps
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            steps+=1
            



        return 


                

            
            
        