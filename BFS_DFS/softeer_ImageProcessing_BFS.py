import sys
from collections import deque
read = sys.stdin.readline

def bfs(i,j,c):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque([])   
    std = graph[i-1][j-1] 
    graph[i-1][j-1] = c
    queue.append([i-1, j-1])
    
    while queue:
        H,W = queue.popleft()
        
        for i in range(4):
            nh = H + dx[i]
            nw = W + dy[i]
            
            if 0<= nh < h and 0<= nw <w and graph[nh][nw] == std:
                graph[nh][nw] = c
                queue.append([nh,nw])
            else:
                continue
           
        
if __name__ == "__main__":
    h,w = map(int, input().split())
    graph = [list(map(int, read().split())) for _ in range(h)]
    q = int(input())
    for _ in range(q):
        i,j,c = tuple(map(int, read().split()))
        if graph[i-1][j-1] != c:
            bfs(i,j,c)
        else:
            continue
            
    for g in graph:
        for col in range(w):
            print(g[col], end =' ')
        print()
    
    
    
