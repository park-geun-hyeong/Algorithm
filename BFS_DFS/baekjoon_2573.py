import sys
from collections import deque
read = sys.stdin.readline

ans = 0 
def dfs(n,m,graph):
    global ans

    drow = [1,-1,0,0]
    dcol = [0,0,1,-1] 
    new_graph = [[0]*m for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            if graph[row][col] != 0:
                cnt = 0 
                for i in range(4):
                    nrow = row + drow[i]
                    ncol = col + dcol[i]
                    
                    if 0<=nrow<n and 0<=ncol<m and graph[nrow][ncol] == 0:
                        cnt += 1
                
                new_graph[row][col] = max(graph[row][col] - cnt, 0)
                    
    cnt = 0 
    check = [[0]*m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if new_graph[row][col] != 0 and check[row][col] == 0:
                cnt += 1
                q = deque([[row,col]])
                check[row][col] = 1
                while q:
                    r,c = q.popleft()
                    
                    for i in range(4):
                        nrow = r + drow[i]
                        ncol = c + dcol[i]

                        if 0<=nrow<n and 0<=ncol<m and new_graph[nrow][ncol] != 0 and check[nrow][ncol] == 0 :
                            check[nrow][ncol] = 1
                            q.append([nrow,ncol])            
                            
    if cnt == 1:
        ans += 1
        dfs(n,m,new_graph)
        return 
        
    elif cnt>1:
        ans += 1
        return
    
    elif cnt == 0:
        ans = 0 
        return 
                       

if __name__ == "__main__":
    n,m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    dfs(n,m,graph)
    
    print(ans)
    
