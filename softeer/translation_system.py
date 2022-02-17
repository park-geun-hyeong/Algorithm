# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=580&sw_prbl_sbms_sn=43814
'''
direction 2 : 아래 -> 위
direction 3 : 오른 -> 왼
direction 0 : 위 -> 아래
direction 1 : 왼 -> 오른

'''
from collections import deque
import sys
read = sys.stdin.readline

def is_in(n,nrow,ncol):
    if 0<=nrow<n and 0<=ncol<n:
        return True
    return False

def return_direc(i):
    if i == 0:
        return 0
    elif i == 1:
        return 2   
    elif i == 2:
        return 1       
    elif i == 3:
        return 3
    
def next_direction(direction, graph, row,col, time):
    order = time%4
    state = graph[row][col][order]
    n = len(graph)
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    next_step = []
    signal = [[0],
              [0,1,2], [1,2,3],[0,1,3],[0,2,3],
              [1,2],[1,3],[0,3],[0,2],
              [0,2], [1,2],[1,3],[0,3]]
    
    
    if direction == (state%4):
        for i in signal[state]:
            nrow = row + move[i][0]
            ncol = col + move[i][1]
            if is_in(n, nrow, ncol):
                direc = return_direc(i)
                next_step.append([nrow, ncol, direc, time+1])
            else:
                continue
                
        if len(next_step) == 0:
            return False
        return next_step
    return False

def bfs(graph,n,t):
    check = [[0]*n for _ in range(n)]
    time = 0
    direction = 2
    q = deque([[0,0, time, direction]]) 
    check[0][0] = 1
    cnt = 1
    ans = set([0,0])
    
    while q:
        row, col, time, direction = q.popleft()
        
        if time == t:
            break
            
        next_step = next_direction(direction, graph, row,col, time)
        if next_step != False:
            for nrow, ncol, direc, T in next_step:
                q.append([nrow,ncol,T,direc])
                if check[nrow][ncol] == 0:
                    check[nrow][ncol] = 1
                    cnt += 1
                
        
    return cnt

if __name__ == "__main__":
    n,t = map(int, read().split())
    if n == 1:
        print(0)
        sys.exit()

    graph = [[0]*n for _ in range(n)]
      
    for row in range(n):
        for col in range(n):
            info = list(map(int, read().split()))
            graph[row][col] = info
            
    print(bfs(graph,n,t))

    
