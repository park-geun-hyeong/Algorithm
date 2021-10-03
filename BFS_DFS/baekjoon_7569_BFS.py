from collections import deque
import sys

def bfs(one:list):
        
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    
    queue = deque(one)
    
    while queue:
        
        z,x,y = queue.popleft() 
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if (0 <= nx <n) and (0<= ny <m) and (0<= nz <h) and (graph[nz][nx][ny] == 0):
                queue.append([nz,nx,ny])
                graph[nz][nx][ny] = graph[z][x][y] + 1
            
            else:
                continue
        

if __name__ == "__main__":
    m,n,h = list(map(int, input().split()))
    graph = [[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)] for _ in range(h)] 
    
    one = [[h,i,j] 
           for h in range(len(graph)) 
           for i in range(len(graph[0])) 
           for j in range(len(graph[0][0])) 
           if graph[h][i][j] == 1] 
    
    isTrue=False
    
    bfs(one)
    max_num=0
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    isTrue=True
                max_num = max(max_num, graph[z][x][y])
                
OBOB    if isTrue == True:
OB        print(-1)
    
OB    else: 
        print(max_num - 1)
OBOB                
                
OB                
