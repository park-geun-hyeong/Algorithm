import sys
from copy import deepcopy
read = sys.stdin.readline
MAX = 0

def move(direction, n, graph):
    
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    new_graph = [[[0,False] for _ in range(n)] for _ in range(n)] 
    
    if direction == 0: #남
        row_range = range(n-1,-1, -1)
        col_range = range(n)
    elif direction == 1 or direction == 3: # 북 or 서
        row_range = range(n)
        col_range = range(n)     
    elif direction == 2: # 동
        row_range = range(n)
        col_range = range(n-1,-1,-1)
     
    for row in row_range:
        for col in col_range:
            if graph[row][col][0] != 0:
                num = graph[row][col][0]
                i = 1
                while True:
                    prev_nrow = row + drow[direction]*(i-1)
                    prev_ncol = col + dcol[direction]*(i-1) 
                    nrow = row + drow[direction]*i
                    ncol = col + dcol[direction]*i
                    if 0<=nrow<n and 0<=ncol<n:
                        if graph[nrow][ncol][0] == 0:
                            i += 1
                            continue
                        
                        elif graph[nrow][ncol][0] == num:
                            if graph[nrow][ncol][1] == True:
                                graph[row][col][0] = 0
                                new_graph[prev_nrow][prev_ncol][0] = num
                                graph[prev_nrow][prev_ncol][0] = num
                                break
                                    
                            if graph[nrow][ncol][1] == False:
                                graph[row][col][0] = 0
                                new_graph[nrow][ncol][0] = num*2
                                graph[nrow][ncol][0] = num*2
                                graph[nrow][ncol][1] = True
                                break
                        #elif graph[nrow][ncol][0] != 0 and graph[nrow][ncol][0] != num:
                        else:
                            graph[row][col][0] = 0
                            new_graph[prev_nrow][prev_ncol][0] = num
                            graph[prev_nrow][prev_ncol][0] = num
                            break
                    #elif nrow<0 or nrow>=n or ncol<0 or ncol>=n:
                    else:
                        graph[row][col][0] = 0
                        new_graph[prev_nrow][prev_ncol][0] = num
                        graph[prev_nrow][prev_ncol][0] = num
                        break   
    
    return new_graph

def solution(cnt, n, graph):
    global MAX
    if cnt >= 5:
        return

    for i in range(4):
        now_graph = deepcopy(graph)
        new_graph = move(i, n, now_graph)
#         if cnt == 0:
#             print("="*10)  
#             for i in range(n):
#                 for j in range(n):
#                     print(new_graph [i][j][0], end =' ')
#                 print()

        MAX = max(MAX, max([new_graph [i][j][0] for i in range(n) for j in range(n)]))
        solution(cnt + 1, n, new_graph )

    return 


if __name__ == "__main__":
    
    n = int(input())
    graph = [list(map(int, read().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            num = graph[i][j]
            graph[i][j] = [num, False]
    
    solution(0, n, graph)
    print(MAX)
    
    
