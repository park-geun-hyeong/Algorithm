import sys
from collections import deque
read = sys.stdin.readline

def melt_check(graph):
    if sum([sum(i) for i in graph]) == 0:
        return True
    return False

def bfs(n,m,i,j,graph,color):
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    check = [[0]*m for _ in range(n)]
    
    q = deque([[i,j]])
    check[i][j] = 1
    graph[i][j] = color

    while q:
        row,col = q.popleft()
        
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            
            if 0<=nrow<n and 0<=ncol<m:
                if graph[nrow][ncol] == 0 and check[nrow][ncol] == 0:
                    check[nrow][ncol] = 1
                    graph[nrow][ncol] = color
                    q.append([nrow,ncol])
            
    return graph
    
def solution(n,m,graph):
    
    cnt = 0 
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]

    while True:
        cand = [[0]*m for _ in range(n)]
        color = 2
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph = bfs(n,m,i,j,graph, color)
                    color += 1
        
        for row in range(n):
            for col in range(m):
                if graph[row][col] == 1:
                    check = 0
                    for i in range(4):
                        nrow = row + drow[i]
                        ncol = col + dcol[i]
                        if 0<=nrow<n and 0<=ncol<m:
                            if graph[nrow][ncol] == 2:
                                check += 1
                                
                    if check<2:
                        cand[row][col] = 1
                        
        
        cnt += 1
        graph = cand
        if melt_check(graph):
            return cnt
    

if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n,m,graph))
    
    
