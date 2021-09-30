import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1] 

    if x<0 or x>=m or y<0 or y>=n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
    
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False


if __name__ == "__main__":
    t = int(input())
    
    info=[]
    for _ in range(t):
        m,n,k = map(int ,input().split())
        location = [list(map(int, input().split())) for _ in range(k)]    
        info.append([[m,n,k], location])
         
    final=[]
    for i in range(t):
        m,n,k = info[i][0]
        location = info[i][1]
        
        graph = [[0] * n for _ in range(m)]
        
        for a,b in location:
            graph[a][b] = 1 
        
        result = 0
        for i in range(m):
            for j in range(n):
                if dfs(i,j) == True:
                    result+=1
                    
        final.append(result)
        
    for i in final:
        print(i)
       
