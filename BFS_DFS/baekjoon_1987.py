import sys
read = sys.stdin.readline
drow = [1,-1, 0, 0]
dcol = [0, 0, 1, -1]

MAX = 1
def dfs(r, c, row, col, trace, cnt):
    global graph, MAX, drow, dcol, loop    
    MAX = max(MAX, cnt)
    if MAX == 26:
        print(MAX)
        sys.exit()
    
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        
        if 0<=nrow<r and 0<=ncol<c:
            loc = ord(graph[nrow][ncol]) - 65
            if trace[loc] == 0:
                trace[loc] = 1
                dfs(r,c,nrow,ncol, trace, cnt + 1)
                trace[loc] = 0              
    return

if __name__ == "__main__":
    r,c = map(int,input().split())
    graph = [list(input()) for _ in range(r)]
    '''
    alpha = set()
    for i in range(r):
        for j in range(c):
            alpha.add(graph[i][j])
    
    trace = dict()
    for i in alpha:
        trace[i] = 0
    
    trace[graph[0][0]] = 1
    
    
    '''
    trace = [0]*26
    trace[ord(graph[0][0]) - 65] = 1
    
    dfs(r,c,0,0, trace, 1)
    print(MAX)
 
    
    
    
