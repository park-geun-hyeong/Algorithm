import sys
from collections import defaultdict
read = sys.stdin.readline

def renewal(graph):
    
    n = len(graph)
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                graph[i][j][1] -= 1
                if graph[i][j][1] == 0:
                    graph[i][j] = 0  
    return graph
    
def move_shark(n, k,graph, direction, priority):
    
    drow = [-1,1,0,0]
    dcol = [0,0,-1,1]
    
    cand = dict()
    for idx in range(1,m+1):
        breaking = 0
        if direction[idx] == -1:
            continue
        for row in range(n):
            if breaking == 1:
                break
            for col in range(n):
                if graph[row][col] == 0:
                    continue
                if breaking == 1:
                    break
                if graph[row][col][0] == idx and graph[row][col][1] == k:
                    state = direction[idx]
                    pr = priority[idx-1][state-1]
                    check = 0
                    for i in pr:
                        nrow = row + drow[i-1]
                        ncol = col + dcol[i-1]
                        
                        if 0<=nrow<n and 0<=ncol<n and graph[nrow][ncol] == 0:
                            check = 1
                            breaking = 1
                            direction[idx] = i
                            cand[idx] = [nrow,ncol]
                            break
                            
                                
                    if check == 0:
                        for i in pr:
                            nrow = row + drow[i-1]
                            ncol = col + dcol[i-1]
                            if 0<=nrow<n and 0<=ncol<n and graph[nrow][ncol][0] == idx:
                                direction[idx] = i
                                cand[idx] = [nrow,ncol]
                                break
                                
    
    graph = renewal(graph)
    for key, value in cand.items():
        row,col = value
        if graph[row][col] == 0:
            graph[row][col]  = [key, k]
        
        if type(graph[row][col]) == list:
            if graph[row][col][0] == key:
                graph[row][col]  = [key, k]
            else:
                direction[key] = -1
    
    return graph, direction

def end_check(direction):
    
    if direction[1] == -1:
        return
    
    for i in range(2, len(direction)+1):
        if direction[i] != -1:
            return False    
    return True
    
    
def solution(n,m,k, graph,direction, priority):
    
    time = 0
    while True:
        graph,direction == move_shark(n,k, graph, direction, priority)
        time += 1
        if end_check(direction) == True:
            break

        if time>=1000:
            return -1
    
    return time

if __name__ == "__main__":
    n,m,k = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                graph[i][j] = [graph[i][j], k]
    
    first = list(map(int, read().split()))
    
    def m_one():
        return -1
    
    direction = defaultdict(m_one)
    for i in range(m):
        direction[i+1] = first[i]
        
        
    priority = [[list(map(int, read().split())) for _ in range(4)] for _ in range(m)]
    
    print(solution(n,m,k, graph,direction, priority))
    
    
    
