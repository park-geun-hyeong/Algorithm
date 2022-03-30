import sys 
from collections import deque
read = sys.stdin.readline
sys.setrecursionlimit(20000)

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
    
def color_dfs(color, n, row, col):
    global color_check, graph
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    color_check[row][col] = 1
    
    for I in range(4):
        nrow = row + drow[I]
        ncol = col + dcol[I]
        
        if 0<=nrow<n and 0<=ncol<n:
            if possible(color, graph[nrow][ncol]) and color_check[nrow][ncol] == 0:
                color_dfs(color, n ,nrow, ncol)
    return 
                
def origin_dfs(color, n, row, col):
    global origin_check, graph
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    origin_check[row][col] = 1
    
    for I in range(4):
        nrow = row + drow[I]
        ncol = col + dcol[I]
        
        if 0<=nrow<n and 0<=ncol<n:
            if graph[nrow][ncol] == color and origin_check[nrow][ncol] == 0:
                origin_dfs(color, n ,nrow, ncol)
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
                color = graph[i][j]
                origin_dfs(color,n,i,j)
                origin_cnt += 1  
            
            if color_check[i][j] == 0:
                color = graph[i][j]
                color_dfs(color,n,i,j)
                color_cnt += 1
    
    print(origin_cnt, color_cnt)
    
    
