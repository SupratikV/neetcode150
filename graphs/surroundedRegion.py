class Solution:
    def solve(self, board: List[List[str]]) -> None:
            rows=len(board)
            cols=len(board[0])
            visit=set()

            def dfs(r,c):
                if r not in range(rows) or c not in range(cols) or board[r][c]!='O' or (r,c) in visit: 
                    return
                visit.add((r,c))
                board[r][c]='L'
                dfs(r+1,c)h
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            
            #cols
            for c in range(cols):
                if board[0][c]=="O":
                    dfs(0,c)

                if board[rows-1][c]=="O":
                    dfs(rows-1,c)
            #rows
            for c in range(rows):
                if board[c][0]=="O":
                    dfs(c,0)

                if board[c][cols-1]=="O":
                    dfs(c,cols-1)

            #finally changin the Os
            for i in range(rows):
                for j in range(cols):
                    if board[i][j]=='O':
                        board[i][j]='X'
                    if board[i][j]=='L':
                        board[i][j]='O'
            
                