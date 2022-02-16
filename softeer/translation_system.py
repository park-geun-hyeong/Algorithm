# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=580&sw_prbl_sbms_sn=43796
import sys
read = sys.stdin.readline

def is_true(n,nrow,ncol):
    if 0<=nrow<n and 0<=ncol<n:
        return True
    return False

def next_direction(direction, graph, row,col, time):
    order = time%4
    state = graph[row][col][order]
    n = len(graph)
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    next_step = []
    signal = [[0],
              [0,1,2], [1,2,3],[0,1,3],[0,2,3],
              [1,2],[1,3],[0,3],[0,2],
              [0,3], [1,2],[1,3],[0,3]]
    
    
    if direction != (state%4):
        return False
    
    direc = 0
    for i in signal[state]:
        nrow = row + move[i][0]
        ncol = col + move[i][1]
        if is_true(n, nrow, ncol):
            if i == 0:
                direc = 0
            elif i == 1:
                direc = 2
            elif i == 2:
                direc = 1
            elif i == 3:
                direc = 3
                
            next_step.append([nrow, ncol, direc])
    
    if len(next_step) == 0:
        return False
    return next_step
            
ans = [[0,0]]
def recursive(direction, graph, row,col, time):
        
    global ans
    global t
    
    if time == t:
        return 

    next_step = next_direction(direction, graph, row,col, time)
    #print(time, next_step)
    if next_step == False:
        return
    
    for nrow, ncol, direc in next_step:
        if [nrow,ncol] not in ans:
            ans.append([nrow, ncol])
        recursive(direc, graph, nrow, ncol, time + 1)

if __name__ == "__main__":
    n,t = map(int, read().split())
    if n == 1:
        print(n)
        sys.exit()

    graph = [[0]*3 for _ in range(n)]
      
    for row in range(n):
        for col in range(n):
            info = list(map(int, read().split()))
            graph[row][col] = info
            
    start_direction = 2
    start_time = 0 
    start_row = 0
    start_col = 0
    
    recursive(start_direction, graph, start_row, start_col, start_time)
    #print(ans)
    print(len(ans))

