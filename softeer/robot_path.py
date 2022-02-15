import sys
from collections import deque
read = sys.stdin.readline

def check_direc(direc, i):
    if direc == i:
        return 'G'
    
    if direc == 0:
        if i == 2:
            return 'L'
        elif i == 3:
            return 'R'
    
    if direc == 1:
        if i == 2:
            return 'R'
        elif i == 3:
            return 'L'
        
    if direc == 2:
        if i == 0:
            return 'R'
        elif i == 1:
            return 'L'
        
    if direc == 3:
        if i == 0:
            return 'L'
        elif i == 1:
            return 'R'

    return None

def solution(h,w,graph):
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    mat = [[1]*w for _ in range(h)]
    start_point = []
    for row in range(h):
        for col in range(w):
            if graph[row][col] == '#':
                mat[row][col] = 0
                check = [0]*4
                for i in range(4):
                    nrow = row + drow[i]
                    ncol = col + dcol[i]
                    if 0<=nrow<h and 0<=ncol<w and graph[nrow][ncol] == '.':
                        check[i] = 1
                    elif nrow<0 or nrow>=h or ncol<0 or ncol>=w:
                        check[i] = 1
                        
                if sum(check) == 3:
                    direction = '_'
                    for i in range(4):
                        if check[i] == 0 and i == 0:
                            direction = 'v'
                        elif check[i] == 0 and i == 1:
                            direction = '^'
                        elif check[i] == 0 and i == 2:
                            direction = '>'
                        elif check[i] == 0 and i == 3:
                            direction = '<'
                            
                    start_point.append([row,col,direction])
    
    using_case = start_point[0]
    
    q = deque([[using_case[0], using_case[1]]])
    move = ''
    direc = 0
    if using_case[2] == 'v':
        direc = 0
    elif using_case[2] == '^':
        direc = 1
    elif using_case[2] == '>':
        direc = 2
    elif using_case[2] == '<':
        direc = 3
    
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    
    drow = [2,-2,0,0]
    dcol = [0,0,2,-2]
    
    while q :
        row, col = q.popleft()
        mat[row][col] = 1
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            
            nr = row+dr[i]
            nc = col+dc[i]
            
            if 0<=nrow<h and 0<=ncol<w and mat[nrow][ncol] == 0 and mat[nr][nc] == 0:
                if check_direc(direc, i) == 'G':
                    move+='A'
                    q.append([nrow,ncol])
                    mat[nr][nc] = 1

                   
                elif  check_direc(direc, i) == 'R':
                    move+='RA'
                    q.append([nrow,ncol])
                    mat[nr][nc] = 1
                    direc = i

                
                elif check_direc(direc, i) == 'L':
                    move+='LA'
                    q.append([nrow,ncol])
                    mat[nr][nc] = 1
                    direc = i

    return using_case, move

if __name__ == "__main__":
    h,w = list(map(int, read().split()))
    graph = [list(map(str,read().rstrip())) for _ in range(h)]
    
    using_case, move = solution(h,w,graph)
    print(using_case[0]+1, using_case[1]+1)
    print(using_case[2])
    print(move)

