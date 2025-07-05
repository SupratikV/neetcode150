class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS=len(heights)
        COLS=len(heights[0])
        pac=set()
        atl=set()
        res=[]

        def dfs(r,c,visit,minheight):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or heights[r][c]<minheight:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
            
        