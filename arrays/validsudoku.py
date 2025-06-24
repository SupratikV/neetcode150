board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
row=set()
column=set()
square=set()

#to check rows
for i in range(len(board)):
    for j in range(9):
        if board[i][j]=='.':
            continue
        if board[i][j] in row:
            print(False,"in row")
        else:
            row.add(board[i][j])
    row=set()

for j in range(len(board)):
    for i in range(9):
        if board[i][j]=='.':
            continue
        if board[i][j] in column:
            print (False,"in column")
        else:
            column.add(board[i][j])
    column=set()

for squares in range(9):
    for i in range(3):
        for j in range(3):
            row=(squares//3)*3+i
            column=(squares%3)*3+j
            if board[row][column]=='.':
                continue
            if board[row][column] in square:
                print (False,"in square")
            square.add(board[row][column])
    square =set()

print (True)
