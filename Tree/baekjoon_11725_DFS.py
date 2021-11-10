import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start, graph, parent):
    
    for i in graph[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i, graph ,parent)
        
if __name__ == "__main__":
    
    n = int(input())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a,b = list(map(int, read().split()))
        graph[a].append(b)
        graph[b].append(a)
     
    parent=[0 for _ in range(n+1)]
    dfs(1, graph, parent)
    
    for i in range(2, n+1):
        print(parent[i])
        

