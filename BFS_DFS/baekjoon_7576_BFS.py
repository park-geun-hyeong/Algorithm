from collections import deque
import sys

def bfs(one:list):
        
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque([i for i in one])
    
    while queue:
        
        x,y = queue.popleft() 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx <n) and (0<= ny <m) and (graph[nx][ny]) == -1:
                continue
            
            elif (0 <= nx <n) and (0<= ny <m) and (graph[nx][ny] == 0):
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
            
            else:
                continue
                
    
    if 1 in [0 in i for i in graph]:
        return '-1'
    
    return max([max(i) for i in graph]) - 1


if __name__ == "__main__":
    m,n = list(map(int, input().split()))
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 
    
    one = [[i,j] for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 1]
    
    if 0 in [0 not in i for i in graph]:
        print(bfs(one))
    else:
        print("0")
