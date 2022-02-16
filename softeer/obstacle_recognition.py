import sys
from collections import deque
read = sys.stdin.readline

def bfs(graph, i, j):
    n=len(graph)
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    q = deque([[i,j]])
    graph[i][j] = 2
    
    cnt = 1 
    while q:
        row,col = q.popleft()
        
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            
            if 0<=nrow<n and 0<=ncol<n and graph[nrow][ncol] == 1:
                q.append([nrow, ncol])
                graph[nrow][ncol] = 2
                cnt += 1
    
    
    return graph, cnt
        

def solution(n,graph):

    ans = []
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                graph, cnt = bfs(graph,i,j)
                ans.append(cnt)
    
    return len(ans), sorted(ans) 


if __name__ == "__main__":
    n = int(read().rstrip())
    graph = [list(map(int, read().rstrip())) for _ in range(n)]
    length, ans = solution(n,graph)
    print(length)
    for i in ans:
        print(i)
    
