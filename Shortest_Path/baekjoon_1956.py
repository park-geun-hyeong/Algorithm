import sys
read = sys.stdin.readline
inf = sys.maxsize 

if __name__ == "__main__":
    v,e = map(int, input().split())
    graph = [[inf]*(v+1) for _ in range(v+1)]
    
    for _ in range(e):
        a,b,c = map(int, input().split())
        graph[a][b] = c
    
    MIN = inf
    for mid in range(1,v+1):
        for start in range(1,v+1):
            for end in range(1,v+1):
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])
                if start == end:
                    MIN = min(MIN, graph[start][end]) 
                    
    if MIN == inf:
        print(-1)
    else:
        print(MIN)
        
