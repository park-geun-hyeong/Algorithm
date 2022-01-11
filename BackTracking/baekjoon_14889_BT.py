import sys 
read = sys.stdin.readline
sys.setrecirsionlimit(20000)

def dfs(idx, cnt):
    global MIN
    
    if cnt == n//2:
        start = 0 
        link = 0 
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                    
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
                    
        MIN = min(MIN, abs(start - link))
        return
                           
    for i in range(idx,n):
        if visited[i]:
            continue
        
        visited[i] = 1
        dfs(idx +1 ,cnt+1)
        visited[i] = 0
        

if __name__ == "__main__":
    n = int(input())
    assert (n%2==0) and (4<=n<=20)     
    graph = [list(map(int, input().split())) for _ in range(n)]
    MIN = 10e9
    visited = [0]*n

    dfs(0, 0)
    print(MIN)
    
    
    
