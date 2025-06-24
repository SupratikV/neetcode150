grid = [[1,0],[1,1]]

rows={}
columns={}
c=0

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column]==1:
            rows[row]=1+rows.get(row,0)
            columns[column]=1+columns.get(column,0)
        else:
            rows[row]=rows.get(row,0)
            columns[column]=columns.get(column,0)

        # try:
        #     if columns[column]>=2 or rows[row]>=2:
        #         c+=1
        # except:
        #     print("error at ",row,column)
        #     print(rows)
        #     print(columns)

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column]==1:
            if rows[row]>=2 or columns[column]>=2:
                c+=1

        
print(c)
print(rows)
print(columns)
    