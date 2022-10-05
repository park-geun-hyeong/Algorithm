from copy import deepcopy
shark = dict()
trace=[]
d_row = [0,-1,0,1,0]
d_col = [0,0,-1,0,1]
drow = [0,0,-1,-1,-1,0,1,1,1]
dcol = [0,-1,-1,0,1,1,1,0,-1]
smell = [[[] for _ in range(4)] for _ in range(4)]

def FishPossible(nrow, ncol):
    global smell, shark
    if 0<=nrow<4 and 0<=ncol<4:    # 범위안에 속할 때
        if len(smell[nrow][ncol]) == 0:   # 냄새가 업는 경우
            if nrow != shark['row'] or ncol != shark['col']:  # 상어가 없는 경우
                return True
            else: 
                return False
        else:
             return False       
    else:
        return False
    
def SharkPossible(row,col,i):
    global d_row, d_col
    
    nrow = row + d_row[i]
    ncol = col + d_col[i]
    
    if 0<=nrow<4 and 0<=ncol<4:
        return True, nrow, ncol
    return False, -1, -1
    
def FishMoving(graph):
    global smell, shark, drow, dcol
  
    new_graph = [[[] for _ in range(4)] for _ in range(4)]
    for row in range(4):
        for col in range(4):
            if len(graph[row][col])>0:
                for i in range(len(graph[row][col])): 
                    idx = graph[row][col][i]
                    check = 0
                    while check<8:
                        nrow = row+drow[idx]
                        ncol = col+dcol[idx]
                        if FishPossible(nrow, ncol):
                            new_graph[nrow][ncol].append(idx)
                            break
                        else:
                            idx-=1
                            if idx < 1:
                                idx = 8
                            check+=1
                    if check == 8:
                        new_graph[row][col].append(graph[row][col][i])
                
    return new_graph

def sharkmoving(graph, row, col, directions, eating_nums, cnt):
    global trace, d_row, d_col
    
    for i in range(1,5):
        possible, nrow, ncol = SharkPossible(row,col,i)
        if possible:
            if len(graph[nrow][ncol])>0:
                if cnt == 2:
                    trace.append((eating_nums+len(graph[nrow][ncol]), directions+str(i)))
                    continue
                else:
                    new_graph = deepcopy(graph)
                    new_graph[nrow][ncol].clear()
                    sharkmoving(new_graph, nrow, ncol, directions+str(i), eating_nums+len(graph[nrow][ncol]), cnt+1)
                    
            else:
                if cnt == 2:
                    trace.append((eating_nums, directions+str(i)))
                    continue
                else:
                    sharkmoving(graph, nrow, ncol, directions+str(i), eating_nums, cnt+1)
        else:
            continue
    return       
    
def removeSmell():
    global smell,shark
    
    for row in range(4):
        for col in range(4):
            if len(smell[row][col])>0:
                if smell[row][col][0] == 2:
                    del smell[row][col][0]
                    if len(smell[row][col])>0:
                        smell[row][col] = [i+1 for i in smell[row][col]]
                else:
                    smell[row][col] = [i+1 for i in smell[row][col]]
                    
def solution(m,s,graph):

    global shark,smell,trace,d_row,d_col
    cnt = m
    before_cnt = m
    
    for _ in range(s):
        new_graph = FishMoving(graph)
  
        row, col = shark['row'], shark['col'] 
        sharkmoving(new_graph, row, col, '',0 ,0)
        trace.sort(key= lambda x :(-x[0], x[1]))

        now_direction = trace[0][1]
        now_eatingNums = trace[0][0]
        trace.clear()
        
        for i in now_direction:
            nrow = row + d_row[int(i)]
            ncol = col + d_col[int(i)]
            if len(new_graph[nrow][ncol])>0:
                new_graph[nrow][ncol].clear()
                smell[nrow][ncol].append(0)
            
            row = nrow
            col = ncol
        
        shark['row'], shark['col'] = row, col

        
        removeSmell()
        cnt-=now_eatingNums
        for row in range(4):
            for col in range(4):
                if len(graph[row][col]) > 0:
                    new_graph[row][col] += graph[row][col]
        
        cnt += before_cnt
        before_cnt = cnt
        graph = new_graph

    return cnt

if __name__ == "__main__":
    
    m,s = map(int, input().split())
    graph = [[[] for _ in range(4)] for _ in range(4)]
    
    for _ in range(m):
        fx, fy, d = map(int, input().split())
        graph[fx-1][fy-1].append(d)     
    
    x,y = map(int, input().split())
    shark['row'] = x-1
    shark['col'] = y-1

    ans = solution(m,s,graph)
    print(ans)
    
