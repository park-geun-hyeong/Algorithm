from collections import deque
import sys

def bfs(x,y,graph):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque([[x,y]])
    graph[x][y] = 1
    
    while queue:
        
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]  
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            else:
                if graph[nx][ny] == 1: 
                        queue.append([nx,ny])
                        graph[nx][ny] = graph[x][y] + 1
                else:
                    continue               
            
    return graph[n-1][m-1]
            
    
if __name__ == "__main__":
    n,m = list(map(int, input().split()))
    graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)] 
    
    print(bfs(0,0,graph))
