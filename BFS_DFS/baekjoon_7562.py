from collections import deque
import sys

def bfs(graph, start_x,start_y, end_x,end_y):
    n = len(graph)
    dy = [-1,-2,1,2,-1,-2,1,2]
    dx = [2,1,2,1,-2,-1,-2,-1]
    
    queue = deque([[start_x,start_y]])
    graph[start_x][start_y] = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if (0 <= nx <n) and (0 <= ny < n) and (graph[nx][ny] == 0):
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[end_x][end_y] -1 

if __name__ == "__main__":
    t = int(input())
    
    num=[]
    for _ in range(t):
        i = int(input())
        start = list(map(int, input().split()))
        end = list(map(int, input().split()))
        
        graph = [[0 for _ in range(i)] for _ in range(i)]
        
        cnt = bfs(graph, start[0], start[1], end[0], end[1])
        num.append(cnt) 
        
    for i in num:
        print(i)
        
        
