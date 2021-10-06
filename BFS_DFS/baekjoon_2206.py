from collections import deque
import sys

def bfs(x,y,z):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque([[x,y,z]]) 
    visited[x][y][z] = 1

    while queue:
        x,y,z = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0<= nx < n) and (0<= ny <m) and (0<=z<=1):
                if (graph[nx][ny] == 0) and (visited[nx][ny][z] == -1):
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx,ny,z])
                    
                elif (z==0) and (graph[nx][ny] == 1) and (visited[nx][ny][z] == -1):
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    queue.append([nx, ny, z+1])
    
    return visited[n-1][m-1][0], visited[n-1][m-1][1]
        
if __name__ == '__main__':
    n,m = list(map(int, input().split()))
    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    
    visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]
    
    ans1, ans2 = bfs(0,0,0)
    
    if ans1 == -1 and ans2 != -1:
        print(ans2)
    elif ans1 != -1 and ans2 == -1:
        print(ans1)
    else:
        print(min(ans1,ans2))
    
    
