import sys
read = sys.stdin.readline
inf = sys.maxsize
        
def solution(n,m,graoh,path):
    
    for mid in range(1,n+1):
        for start in range(1,n+1):
            if start == mid:
                continue
            for end in range(1, n+1):
                if end == mid:
                    continue
                
                if graph[start][end]> graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]
                    path[start][end] = path[mid][end]
                    
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(0 if graph[i][j] == inf else graph[i][j], end = ' ')
        print()
    
    for start in range(1,n+1):
        for end in range(1,n+1):
            if graph[start][end] == inf or start == end:
                print(0)
                continue
            else:
                ans=[end]
                while end!=start:
                    ans.append(path[start][end])
                    end = path[start][end]
                    
                print(len(ans), end = " ")
                for p in ans[::-1]:
                    print(p, end = " ")
                print()
                
    
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[inf]*(n+1) for _ in range(n+1)]
    path = [[0]*(n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        graph[i][i] = 0
    
    for _ in range(m):
        a,b,c = map(int, input().split())
        if c < graph[a][b]:
            graph[a][b] = c
            path[a][b] = a
            
    solution(n,m,graph,path)
        
