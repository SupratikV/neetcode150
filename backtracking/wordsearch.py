class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=set()
        ROWS=len(board)
        COLS=len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True

            if (r<0 or r>=ROWS or c<0 or c>=COLS \
             or  board[r][c]!=word[i] or (r,c) in path):
                return False
            
            path.add((r,c))
            res=(dfs(r,c+1,i+1) or dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or\
            dfs(r,c-1,i+1))
            path.remove((r,c))

            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False


        