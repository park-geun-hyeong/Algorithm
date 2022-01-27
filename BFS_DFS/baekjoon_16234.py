import sys
from collections import deque
read = sys.stdin.readline

def open_possible(l,r,country1, country2):
    if l <= abs(country1 - country2) <= r:
        return True
    return False

def bfs(l,r,row,col,graph,check):
        
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    team = [[row,col]]
    q = deque([[row,col]])
    check[row][col] = 1
    
    while q:
        row,col = q.popleft()
        
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0<=nrow<n and 0<=ncol<n and check[nrow][ncol] == 0:
                if open_possible(l,r,graph[row][col], graph[nrow][ncol]):
                    check[nrow][ncol] = 1
                    team.append([nrow,ncol])
                    q.append([nrow,ncol])
    
    return (team,check)
        
        
def solution(n,l,r, graph):
    
    cnt = 0
    check = [[0]*n for _ in range(n)]

    while True:
        check = [[0]*n for _ in range(n)]
        teams = []
        for row in range(n):
            for col in range(n):
                if check[row][col] == 0:
                    team, check = bfs(l,r,row,col,graph,check)
                    if len(team) > 1:
                        teams.append(team)
        
        if len(teams) == 0:
            break
            
        for t in teams:
            new_num = int(sum([graph[row][col] for row, col in t]) / len(t))
            for row, col in t:
                graph[row][col] = new_num
                
        cnt += 1
        
    return cnt

if __name__ == "__main__":
    n,l,r = list(map(int, input().split()))
    graph = [list(map(int, read().split())) for _ in range(n)]
    
    print(solution(n,l,r,graph))
    
    
    
