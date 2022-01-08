import sys
from itertools import product
read= sys.stdin.readline

def with_Row(row):
    if row<3:
        with_row = [0,1,2]
    elif row<6:
        with_row = [3,4,5]
    else: 
        with_row = [6,7,8]
    
    return with_row

def with_Col(col):
    if col<3:
        with_col = [0,1,2]
    elif col<6:
        with_col = [3,4,5]
    else: 
        with_col = [6,7,8]
    
    return with_col

def check_square(i, row, col):
    
    with_row = with_Row(row)
    with_col = with_Col(col)
    
    loc = tuple(product(with_row,with_col))
    
    square = [] 
    for r,c, in loc:
        square.append(graph[r][c])
    
    if i not in square:
        return True
    else:
        return False
           
        
def dfs(depth):
    
    if depth == 10:
        return
    
    for col in range(9):      
        for row in range(depth):
            if graph[row][col] == 0:
                for i in range(1, 10):
                    if (i in ROW[row]) or (i in COL[col]) or (check_square(i,row,col) == False):
                        continue
                   
                    else:
                        graph[row][col] = i
                        ROW[row][col] = i
                        COL[col][row] = i
                        dfs(depth + 1)
            else: 
                continue
                
if __name__ == "__main__":
    
    graph = [list(map(int, input().split())) for _ in range(9)]
    
    ROW = graph
    COL = [[] for _ in range(9)] # transpose
    for i in ROW:
        for j in range(9):
            COL[j].append(i[j])
             
    dfs(1)
    print()
    for i in graph:
        print(' '.join(map(str, i)))
    

