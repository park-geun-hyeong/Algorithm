import sys
from collections import deque
read = sys.stdin.readline

def short_path(start_row, start_col, size, graph):
    n = len(graph)
    q = deque([[start_row, start_col]])
    
    check = [[0]*n for _ in range(n)]
    path_graph = [[0]*n for _ in range(n)]
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    foods = []
    check[start_row][start_col] = 1

    dist = 0
    state = 0
    while q:
        if state == 1:
            break
            
        row, col = q.popleft()
        
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0<=nrow<n and 0<=ncol<n and graph[nrow][ncol]<=size and check[nrow][ncol] == 0:
                q.append([nrow,ncol])
                check[nrow][ncol] = 1
                path_graph[nrow][ncol] = path_graph[row][col] + 1 
                
                if 0 < graph[nrow][ncol] < size:
                    if dist == 0:
                        dist = path_graph[nrow][ncol]
                    elif path_graph[nrow][ncol] > dist:
                        state = 1
                        break
                    foods.append([path_graph[nrow][ncol],nrow, ncol])
                    
            
    if len(foods) == 0:
        return False
    return sorted(foods, key = lambda x: (x[0],x[1],x[2]))[0]        
            
    
def solution(n,graph):
    
    s_row = 0
    s_col = 0
    state = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                s_row = i
                s_col = j
            if graph[i][j] == 1:
                state = 1
                
    if state == 0:
        return 0
    
    size = 2
    time = 0
    food_num = 0
    while True:
        
        food = short_path(s_row, s_col, size, graph)
        if food == False:
            break
        
        t, f_r, f_c = food    
        time += t
        
        food_num += 1
        if food_num == size:
            food_num = 0
            size += 1
            
        graph[s_row][s_col] = 0
        graph[f_r][f_c] = 9
        s_row = f_r
        s_col = f_c 
            
    return time

if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, read().split())) for _ in range(n)]
    print(solution(n,graph))
    
    
