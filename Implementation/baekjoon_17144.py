import sys 
from copy import deepcopy
read = sys.stdin.readline

def up_loc(s_r,r,c,row,col):
    if row == 0 and col!=0:
        return row,col-1
    if row ==s_r and col != c-1:
        return row, col+1
    if col == c-1:
        return row-1, col
    if col == 0:
        return row+1, col
    
def down_loc(s_r,r,c,row,col):
    if row == s_r and col != c-1:
        return row, col+1
    if row == r-1 and col != 0:
        return row, col-1
    if col == c-1:
        return row+1, col
    if col == 0:
        return row -1, col

def cleaning(loc, r,c,graph):
    
    new_graph = deepcopy(graph)
    up_row, up_col = loc[0]
    down_row, down_col = loc[1]
    
    start_up_row = up_row 
    start_up_col = up_col + 1
    start_down_row = down_row
    start_down_col = down_col + 1
    
    new_graph[start_up_row][start_up_col] = 0
    new_graph[start_down_row][start_down_col] = 0
    
    flag1=False 
    flag2=False 
    while True:
        
        if not flag1:
            nxt_up_row, nxt_up_col = up_loc(up_row,r,c,start_up_row, start_up_col)
            if nxt_up_row == up_row and nxt_up_col == up_col:
                flag1= True
            else: 
                new_graph[nxt_up_row][nxt_up_col] = graph[start_up_row][start_up_col]
        
        if not flag2: 
            nxt_down_row, nxt_down_col = down_loc(down_row,r,c,start_down_row, start_down_col)
            if nxt_down_row == down_row and  nxt_down_col == down_col:
                flag2= True
            else:
                new_graph[nxt_down_row][nxt_down_col] = graph[start_down_row][start_down_col]
     
        if flag1 and flag2:
            break
        
        start_up_row = nxt_up_row
        start_up_col = nxt_up_col
        start_down_row = nxt_down_row
        start_down_col = nxt_down_col
        
    return new_graph

def difusion(loc,r,c,graph):
    
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    new_graph = [[0]*c for _ in range(r)]
    new_graph[loc[0][0]][loc[0][1]] = -1
    new_graph[loc[1][0]][loc[1][1]] = -1
    
    for row in range(r):
        for col in range(c):
            if graph[row][col]>=1:
                cnt = 0
                for i in range(4):
                    nrow = row+drow[i]
                    ncol = col+dcol[i]
                    
                    if 0<=nrow<r and 0<=ncol<c and graph[nrow][ncol] != -1:
                        cnt += 1
                        new_graph[nrow][ncol] += graph[row][col] // 5
                
                new_graph[row][col] += graph[row][col] - (graph[row][col]//5)*cnt
            
    return new_graph


def solution(r,c,t, graph):
    
    loc = []
    for row in range(r):
        for col in range(c):
            if graph[row][col] == -1:
                loc.append([row,col])
                loc.append([row+1, col])
                break
    
    for _ in range(t):
        graph = difusion(loc,r,c,graph)
        graph = cleaning(loc,r,c,graph)
        
    return sum([sum(i) for i in graph]) + 2


if __name__ =="__main__":
    r,c,t = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(r)]
    #graph = [[0, 0, 0, 0, 0, 0, 0, 9],[0, 0, 0, 0, 3, 0, 0, 8],[-1, 0, 5, 0, 0, 0, 22, 0],[-1, 8, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 10, 43, 0],[0, 0, 5, 0, 15, 0, 0, 0],[0, 0, 40, 0, 0, 0, 20, 0]]

    ans = solution(r,c,t, graph)
    print(ans)
    
    
