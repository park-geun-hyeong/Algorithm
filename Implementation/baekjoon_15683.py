import sys
from itertools import product
from copy import deepcopy
read = sys.stdin.readline

drow = [1,-1,0,0]
dcol = [0,0,1,-1]
    
def blind_spot(graph):
    return sum([i.count(0) for i in graph]) 

def move(n,m,row,col, drow, dcol,graph):
    
    num = graph[row][col]
    while True:
        row += drow
        col += dcol
        
        if row<0 or row>=n or col<0 or col>=m or graph[row][col] == 6:
            break
        if graph[row][col] in (1,2,3,4,5):
            continue
        graph[row][col] = num
        
    return graph

def cctv(n,m,row,col,direction, graph):
    global drow,dcol
    
    for i in direction:
        graph = move(n,m,row,col,drow[i],dcol[i], graph)
        
    return graph
    
def solution(n,m,graph):
    five_loc = [] 
    location = []  
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 6 or graph[i][j] == 0:
                continue
            elif graph[i][j] == 5:
                five_loc.append([i,j])
            elif graph[i][j] == 2:
                p = []
                for k in range(2):
                    p.append([2, k,i,j])
                location.append(p)
            else:
                p = []
                for k in range(4):
                    p.append([graph[i][j],k,i,j])
                location.append(p)
             
    cases = list(product(*location))
    
    directions = [[],
            [[0],[1],[2],[3]],
            [[0,1],[2,3]],
            [[1,2],[0,2],[0,3],[1,3]],
            [[1,2,3],[0,1,2],[0,2,3],[0,1,3]],
            [[0,1,2,3]]]
    
    if len(five_loc) != 0:
        for row,col in five_loc:
            graph = cctv(n,m,row,col, directions[5][0], graph)
    
    Min = 1e9
    for case in cases:
        graph_copy = deepcopy(graph)
    
        for cctv_num, direction, row,col in case:
            graph_copy = cctv(n,m,row,col, directions[cctv_num][direction], graph_copy)
        Min = min(Min, blind_spot(graph_copy))
        if Min == 0:
            return 0
    
    return Min 

if __name__ == "__main__":
    n,m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]    
    print(solution(n,m,graph))
    
    
