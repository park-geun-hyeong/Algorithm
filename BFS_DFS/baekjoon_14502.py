import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
read = sys.stdin.readline

def bfs(graph, virus_loc):
    n=len(graph)
    m=len(graph[0])
    
    graph_c = deepcopy(graph)
    q = deque(virus_loc)
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    
    while q:
        row,col = q.popleft()
        
        for i in range(4):
            nrow = row+dx[i]
            ncol = col+dy[i]
            
            if 0<=nrow<n and 0<=ncol<m and graph_c[nrow][ncol] == 0:
                graph_c[nrow][ncol] = 2
                q.append([nrow, ncol])               
    
    return sum([i.count(0) for i in graph_c])
                

def solution(n,m,graph):
    zero_loc = []
    virus_loc = []
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 0:
                zero_loc.append([row,col])
            elif graph[row][col] == 2:
                virus_loc.append([row,col])
    
    safety_zone=[]
    add_point = list(combinations(zero_loc, 3))
    for case in add_point:
        for loc in case:
            row,col = loc
            graph[row][col] = 1
       
        safety_zone.append(bfs(graph, virus_loc))
        
        for loc in case:
            row, col = loc
            graph[row][col] = 0
                
    
    print(max(safety_zone))
            

if __name__ == "__main__":
    n,m = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution(n,m,graph)
     
