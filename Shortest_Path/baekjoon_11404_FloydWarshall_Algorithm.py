import sys
inf = sys.maxsize
read = sys.stdin.readline

def short(graph):
    
    n = len(graph) - 1
    for i in range(1, n+1): ## i ==> 중간에 거치는 지점
        for j in range(1, n+1):
            for k in range(1, n+1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    
    for a in range(1, n+1):
        for b in range(1, n+1): 
            if graph[a][b] == inf:
                print(0, end = ' ')
            else:
                print(graph[a][b],  end =' ')         
        print()
        
    
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    graph = [[inf] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
                        
    for _ in range(m):
        a,b,c = map(int, read().split())
        if graph[a][b] == inf:
            graph[a][b] = c
        else:
            if c < graph[a][b]:
                graph[a][b] = c
            else:
                continue        
        
    short(graph)
