from collections import deque
import sys

def graph(n, line):
    Graph = [[] for _ in range(n+1)]
    
    for j in line:
        for i in range(1, n+1):
            if j[0] == i:
                Graph[i].append(j[1])
            elif j[1] == i:
                Graph[i].append(j[0])
            else: 
                continue
         
    return [sorted(i) for i in Graph]

def dfs(Graph, v, visited):
    
    visited[v] = True
    print(v, end = ' ')
     
    for i in Graph[v]:
        if not visited[i]:
            dfs(Graph, i ,visited)
            
            
    
def bfs(Graph, start, visited):
    
    queue = deque([start])
    
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        
        for i in Graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
    
if __name__ == '__main__':
    n,m,v = map(int, input().split())
    line = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    Graph = graph(n,line)
    
    visited = [False] * (n+1)
    dfs(Graph, v, visited)
    print()
    
    visited = [False] * (n+1)
    bfs(Graph, v, visited)
    
    
