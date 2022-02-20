import sys
from copy import deepcopy
read = sys.stdin.readline


def move_fish(graph):
    
    drow = [-1,-1,0,1,1,1,0,-1]
    dcol = [0,-1,-1,-1,0,1,1,1]
    
    for idx in range(1,17):
        breaking = 0
        for row in range(4):
            if breaking == 1:
                break
            for col in range(4):
                if breaking == 1:
                    break
                if graph[row][col][0] == idx:
                    breaking = 1
                    state = graph[row][col][1] - 1
                    for plus in range(8):
                        loc = (state + plus)%8
                        nrow = row + drow[loc]
                        ncol = col + dcol[loc]
                        if 0<=nrow<4 and 0<= ncol<4 and graph[nrow][ncol][0] != -1:
                            temp = graph[nrow][ncol]
                            graph[nrow][ncol] = [idx, loc+1]
                            graph[row][col] = temp
                            break
                        else:
                            continue
        
    return graph

ans = []
def move_shark(num, graph):

    global ans
    
    graph = move_fish(graph)

    drow = [-1,-1,0,1,1,1,0,-1]
    dcol = [0,-1,-1,-1,0,1,1,1]
    
    breaking = 0 
    row = 0
    col = 0
    state = 0
    for i in range(4):
        if breaking == 1:
            break
        for j in range(4):
            if graph[i][j][0] == -1:
                row = i
                col = j
                state = graph[i][j][1] - 1 
                breaking = 1
                break
    
    dr = drow[state]
    dc = dcol[state]
    
    for i in range(1,4):
        
        nrow = row+dr*i
        ncol = col+dc*i
        
        if 0<=nrow<4 and 0<=ncol<4 and graph[nrow][ncol][0] > 0:
            
            food = graph[nrow][ncol][0]
            new_state = graph[nrow][ncol][1]
            
            graph_c = deepcopy(graph)
            
            graph_c[row][col] = [0,0]
            graph_c[nrow][ncol] = [-1, new_state]
            move_shark(num+food, graph_c)
            continue
            
            
        if 0<=nrow<4 and 0<=ncol<4 and graph[nrow][ncol][0] == 0:
            continue
            
        if nrow<0 or nrow>=4 or ncol<0 or ncol>=4:
            ans.append(num)
            return


if __name__ == "__main__":
    
    graph = [[0]*4  for _ in range(4)]
    for i in range(4):
        arr = list(map(int, read().split()))
        for j in range(4):
            graph[i][j] = arr[j*2:j*2+2]
    
    first_num = graph[0][0][0]
    first_state = graph[0][0][1]
    graph[0][0] = [-1, first_state]
    
    move_shark(first_num, graph)
    
    print(max(ans))
    
    
