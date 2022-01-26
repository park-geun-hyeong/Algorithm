import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
read = sys.stdin.readline

def dfs(graph ,nrow, ncol, drow ,dcol):
    nrow += drow
    ncol += dcol
    if 0<=nrow<n and 0<=ncol<n and (graph[nrow][ncol] == 'X' or graph[nrow][ncol] == 'T'):
        graph[nrow][ncol] = 'T'
        if dfs(graph, nrow, ncol, drow, dcol) == False:
            return False
    elif 0<=nrow<n and 0<=ncol<n and graph[nrow][ncol] == 'O':
        return
    elif 0<=nrow<n and 0<=ncol<n and graph[nrow][ncol] == 'S':
        return False
    
    return
        
def bfs(graph, teacher_loc):
    
    n = len(graph)
    q= deque(teacher_loc)
    graph_c = deepcopy(graph)
    
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    while q:
        row, col = q.popleft()
        
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0<=nrow<n and 0<=ncol<n and (graph_c[nrow][ncol] == 'X' or graph_c[nrow][ncol] == 'T'):
                graph_c[nrow][ncol] = 'T'
                if dfs(graph_c, nrow, ncol, drow[i], dcol[i]) == False:
                    return False
                
            elif 0<=nrow<n and 0<=ncol<n and graph_c[nrow][ncol] == 'O':
                continue
            elif 0<=nrow<n and 0<=ncol<n and graph_c[nrow][ncol] == 'S':
                return False
    
    return True
    

def solution(n,graph):
    wall_loc = []
    teacher_loc = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                wall_loc.append([i,j])
            if graph[i][j] == 'T':
                teacher_loc.append([i,j])
                
                
    wall_case = list(combinations(wall_loc, 3))
    
    for case in wall_case:
        for loc in case:
            row, col = loc
            graph[row][col] = 'O'
            if bfs(graph, teacher_loc):
                return 'YES'
            
        for loc in case:
            row, col = loc
            graph[row][col] = 'X'
    
    return 'NO'
    

if __name__ == "__main__":
    n = int(input())
    graph = [list(map(str, read().split())) for _ in range(n)]
    print(solution(n, graph))
    
