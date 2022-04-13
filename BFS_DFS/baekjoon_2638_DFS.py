import sys
from collections import deque
read = sys.stdin.readline
sys.setrecursionlimit(20000)

def melt_check(graph):
    if sum([sum(i) for i in graph]) == 0:
        return True
    return False

def dfs(graph, n,m,row,col,color):
    
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    graph[row][col] = color

    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]

        if 0<=nrow<n and 0<=ncol<m:
            if graph[nrow][ncol] == 0:
                graph = dfs(graph, n,m,nrow,ncol,color)
                     
    return graphvi

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
                    graph = dfs(graph, n,m,i,j,color)               
                    color += 1
        
        for row in range(n):
            for col in range(m):
                if graph[row][col] == 1:
                    air = 0
                    for i in range(4):
                        nrow = row + drow[i]
                        ncol = col + dcol[i]
                        if 0<=nrow<n and 0<=ncol<m:
                            if graph[nrow][ncol] == 2:
                                air += 1
                                
                    if air<2:
                        cand[row][col] = 1
                        
        
        cnt += 1
        graph = cand
        if melt_check(graph):
            return cnt
    

if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n,m,graph))
    
    
