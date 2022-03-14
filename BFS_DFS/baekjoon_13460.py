import sys
from collections import deque
read = sys.stdin.readline

def move(graph,r,c,dr,dc):
    CNT = 0
    while graph[r+ dr][c+dc] != '#' and graph[r][c] != 'O':        
        r += dr
        c += dc
        CNT += 1
    
    return r, c, CNT

def solution(n,m,graph):
    rr,rc,br,bc = 0,0,0,0

    visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 'R':
                rr = row
                rc = col
                #graph[row][col] = '.'
            elif graph[row][col] == 'B':
                br = row
                bc = col
                #graph[row][col] = '.'

    visited[rr][rc][br][bc] = 1

    drow = [1,-1, 0,0]
    dcol = [0,0,1,-1]
    q = deque([[rr,rc, br, bc, 0]])

    while q:

        red_row, red_col, blue_row, blue_col, cnt = q.popleft()

        if cnt >10:
            return -1

        for i in range(4):
            n_rr,n_rc, r_cnt = move(graph, red_row, red_col, drow[i], dcol[i])
            n_br,n_bc, b_cnt = move(graph, blue_row, blue_col, drow[i], dcol[i])

            if graph[n_br][n_bc] != 'O':              
                if graph[n_rr][n_rc] == 'O':
                    if cnt + 1 >10:
                        return -1
                    return cnt + 1

                if n_rr == n_br and n_rc == n_bc:
                    if r_cnt<b_cnt:
                        n_br -= drow[i]
                        n_bc -= dcol[i]

                    elif b_cnt<r_cnt:
                        n_rr -= drow[i]
                        n_rc -= dcol[i]

                if visited[n_rr][n_rc][n_br][n_bc] == 0:
                    q.append([n_rr, n_rc, n_br, n_bc, cnt + 1])
                    visited[n_rr][n_rc][n_br][n_bc] = 1                  

    return -1 

if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = [list(map(str, input())) for _ in range(n)]
    
    print(solution(n,m,graph))
    
    
     
