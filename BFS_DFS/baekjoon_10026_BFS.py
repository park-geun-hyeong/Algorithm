import sys 
from collections import deque
read = sys.stdin.readline

def possible(color, graph_color):
    if color == 'R':
        if graph_color == 'R' or graph_color == 'G':
            return True
    elif color == 'G':
        if graph_color == 'R' or graph_color == 'G':
            return True
    else:
        if color == graph_color:
            return True
    return False
    
def color_bfs(n,i, j):
    global color_check ,grpah
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    q = deque([[i,j]])
    color = graph[i][j]
    color_check[i][j] = 1
    
    while q:
        row, col = q.popleft()
        
        for I in range(4):
            nrow = row + drow[I]
            ncol = col + dcol[I]
            
            if 0<=nrow<n and 0<=ncol<n:
                if possible(color, graph[nrow][ncol]) and color_check[nrow][ncol] == 0:
                    q.append([nrow,ncol])
                    color_check[nrow][ncol] = 1

    return
                
def origin_bfs(n,i,j):
    global origin_check, graph
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    q = deque([[i,j]])
    color = graph[i][j]
    origin_check[i][j] = 1
    
    while q:
        row, col = q.popleft()
        
        for I in range(4):
            nrow = row + drow[I]
            ncol = col + dcol[I]
            
            if 0<=nrow<n and 0<=ncol<n:
                if graph[nrow][ncol] == color and origin_check[nrow][ncol] == 0:
                    q.append([nrow,ncol])
                    origin_check[nrow][ncol] = 1

    return 

if __name__ == "__main__":
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    origin_check = [[0]*n for _ in range(n)]
    color_check = [[0]*n for _ in range(n)]
    
    origin_cnt = 0
    color_cnt = 0
    for i in range(n):
        for j in range(n):
            if origin_check[i][j] == 0:
                origin_bfs(n,i,j)
                origin_cnt += 1  
            
            if color_check[i][j] == 0:
                color_bfs(n,i,j)
                color_cnt += 1
    
    print(origin_cnt, color_cnt)
    
    
